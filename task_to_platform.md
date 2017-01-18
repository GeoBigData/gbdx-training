## contents
Intro

[step 1) write and test algorithm that processes locally](#step-1-write-and-test-algorithm-that-processes-locally)

[step 2) modify to match I/O structure within Docker container](#step-2-modify-script-to-match-io-structure-within-docker-container)

[step 3) prepare Docker Hub repository](#step-3-prepare-docker-hub-repository)

[step 4) docker: write, build, test, and push](#step-4-docker-write-build-test-and-push)

[step 5) write JSON task definition](#step-5-write-json-task-definition)

[step 6) register and test your task within a workflow using gbdxtools](#step-6-register-and-test-your-task-within-a-workflow-using-gbdxtools)

# Intro
This tutorial...
- demonstrates how to put a very simple task on the platform 
- presumes user has a gbdx account, has installed gbdxtools including config file, has installed docker, registered for a Docker Hub account, and is familiar with python [check READ.ME for instructions](README.md)
- presumes user has previous exposure to AWS, Docker, and GBDX APIs concepts (workflow, tasks, etc..)

## (put a pretty diagram of platform architecture here)
- data storage and processing occurs in AWS
- platform orchestrates movement and processing of data within AWS
- by placing your algorithm within a Docker and registering the image on Docker Hub, the platform is able to retrieve, build, and execute your algorithm within the Workflow system
- you can then process data in concert with other data and algorithms to execute an entire Workflow

## step 1) write and test algorithm that processes locally 
- write and test a script locally 
- here's an example python script that I've labelled clip_raster_task.py 
	- function that clips a raster image using a shapefile
	- default is to clip and output the raster within the bounds of the shapefile. If specify 'exclude' as value for the 	       composition parameter, this function will clip and output the raster outside of the shapefile.  

```python
import fiona
import rasterio
import os
import glob

in_path = os.path.join(os.path.expanduser('~'), 'documents', 'demo', 'input')

shape_path = in_path + '/shapefile'
my_shape = glob.glob(in_path + '/*.shp')

image_path = in_path + '/image' 
my_image = glob.glob(in_path + '/*.tif')
  
out_path = os.path.join(os.path.expanduser('~'), 'documents', 'demo', 'output')

os.makedirs(out_path)
os.chdir(out_path)
  
with fiona.open(shapefile, "r") as shape:
  features = [feature["geometry"] for feature in shape]

with rasterio.open(image) as src:
  out_image, out_transform = rasterio.tools.mask.mask(src, features, crop=True)
  out_meta = src.meta.copy()

out_meta.update({"driver": "GTiff",
  "height": out_image.shape[1],
  "width": out_image.shape[2],
  "transform": out_transform})

with rasterio.open("masked.tif", "w", **out_meta) as dest:
  dest.write(out_image)
```
  
## step 2) modify script to match I/O structure within Docker container
- when you ultimately run your task within a Workflow, via Postman or gbdxtools, the Platform will:
	- pull your Docker image and spin up the Docker container, data, and compute resources
	- fetch your data from a specified S3 location and plug the data into this input port `/mnt/work/input/<your input 	     directory>` (you'll specify this S3 location when you set up your task within a Workflow, more on this later)
	- outputs the results to this output port `/mnt/work/output/<your output directory>`
- the name you give the input and output directories within your script carries over to how you set your data inputs and outputs within a Workflow

	*example using 'image' as the input directory name*

	clip_raster_task.py
	```python
	in_path = '/mnt/work/input/image'
	```
	my_workflow.py 
	```python
	clip_task = gbdx.Task('demo_task', image='s3://<path to S3 location of data') 
	```

- modify the input and output filepaths within your script to mimic those of the Docker ports

```python
import fiona
import rasterio
import os
import glob

#in_path = os.path.join(os.path.expanduser('~'), 'documents', 'demo', 'input')
in_path = '/mnt/work/input'

shape_path = in_path + '/shapefile' 
my_shape = glob.glob(shape_path + '/*.shp')

image_path = in_path + '/image' 
my_image = glob.glob(in_path + '/*.tif')
  
# out_path = os.path.join(os.path.expanduser('~'), 'documents', 'demo', 'output')
out_path = '/mnt/work/output/data_out'

os.makedirs(out_path)
os.chdir(out_path)

with fiona.open(shapefile, "r") as shape:
  features = [feature["geometry"] for feature in shape]

with rasterio.open(image) as src:
  out_image, out_transform = rasterio.tools.mask.mask(src, features, crop=True, invert=invert_property)
  out_meta = src.meta.copy()

out_meta.update({"driver": "GTiff",
  "height": out_image.shape[1],
  "width": out_image.shape[2],
  "transform": out_transform})

with rasterio.open("masked.tif", "w", **out_meta) as dest:
  dest.write(out_image)
```

## step 3) prepare Docker Hub repository
- register for free acount on [Docker Hub](https://hub.docker.com/)
- create a repository for your algorithm 
- [add platform collaborators](screenshots/add_collaborators.png), which will allow the platform to pull and execute your image during a workflow: `tdgpbuild`, `tdgpdeploy`, `tdgplatform` 
	
## step 4) docker: write, build, test, and push  

### write 
- a Dockerfile contains the set of instructions to build a Docker image
- this Docker image will contain your scripts, along with the OS, libraries and dependencies needed to execute your script
- a good practice is to place scripts within a /bin directory that lives next to the Dockerfile
  - my_docker_project/bin/clip_raster.py 
  - my_docker_project/Dockerfile 
- include the following code in a file named `Dockerfile` (no extension)

```
FROM ubuntu:latest

RUN apt-get update && apt-get -y install\
    python \  	
    vim\
    build-essential\
    python-software-properties\
    software-properties-common\
    python-pip\
    python-dev\
    python-numpy\
    wget\
    git\
    cython\
    python-pytest\
    python-nose

RUN wget http://download.osgeo.org/gdal/CURRENT/gdal-2.1.2.tar.gz
RUN tar -xzf gdal-2.1.2.tar.gz
RUN cd gdal-2.1.2; ./configure --enable-debug; make; make install

RUN pip install fiona

RUN git clone https://github.com/mapbox/rasterio.git
RUN cd rasterio; pip install -e .

RUN mkdir /demo
ADD ./bin /demo
CMD python /demo/clip_raster_task.py 
```

- these instructions will build a Docker container with a fresh Ubuntu installation, install libraries and dependencies, create a directory, place your clip_raster_task.py script inside it, and execute the script when a container is built from that Docker image

### build 
- navigate to the directory containing your Dockerfile and use the following command within a Docker session to build the Docker image `docker build -t <docker username>/<docker repository> .`  (note '.' at end of command)(note, this may take several minutes the first time)
- use the command `docker images` to see if your image was successfully built 
- you can now 
	- run a Docker container from that image `docker run -it <docker username>/<docker repository> bash` 
	- navigate within the container like you would any Linux system, see your scripts, and `exit` to return to your 	Docker session

### test 
- the platform will pull and run your algorithm along with data from an S3 location during runtime, but an easy way to test that your algorithm executes as expected is to first run the container with locally mounted data 

`docker run -v ~/<full path to input directory>:/mnt/work/input/data_in -it <docker username>/<docker repository> bash`

- once inside the container, check that your data exists at `/mnt/work/input/data_in`, then navigate to your script and execute it 'python clip_register.py'
- if successful, you should be able to navigate to `/mnt/work/output/data_out` and see your output 
- if needed, modify the original script, build from Dockerfile again, run the container with mounted test data, and test your script until it produces the expected output 

### push
- while still within the Docker session, pass in your Docker Hub credentials
`docker login --username <docker username> --password <docker password>`
- push the image to your Docker Hub repository
`docker push <docker username>/<docker repository>`

## step 5) write JSON task definition 
- to register your task on the platform, first write a task definition according to the following JSON template
- the definition will specify everything the platform needs to know to pull and run your task
```json
{
    "inputPortDescriptors": [
        {
            "required": true,
            "description": "Directory containing image",
            "name": "",
            "type": "string"
        },
        {
            "name": "dependency_input",
            "type": "string"
        }
    ],
    "outputPortDescriptors":[
        {
            "name": "dependency_output",
            "type": "string",
            "multiplex": true
        }
    ],
    "containerDescriptors": [
        {
            "type": "DOCKER",
            "command": "",
            "properties": {
                "image": "<docker username>/<docker repository>",
                "mounts": [
                    {
                        "local": "$task_data_dir",
                        "container": "/mnt/work",
                        "read_only": false
                    }
                ]
            }
        }
    ],
    "description": "Clips a raster to shapefile.",
    "name": "demo_task_<your_intials>",
    "version": "0.0.1",
    "properties": null
}

{
    "name": "demo_task<your_initials>",
    "description": "clips a raster to a shapefile",
    "properties": {
        "isPublic": false,
        "timeout": 7200
    },
    "inputPortDescriptors": [
		{
			"required": true,
			"type": "directory",
			"description": "s3 location of image and shapefile",
			"name": "data_in"
		},
		{
			"required": true,
			"type": "string",
			"description": "Index to calculate - 'NDMI' or 'MNDWI'",
			"name": "index"
		}
    ],
    "outputPortDescriptors": [
		{
			"required": true,
			"type": "directory",
			"description": "s3 output location",
			"name": "data_out"
		}
    ],
    "containerDescriptors": [
		{
			"type": "DOCKER",
			"command": "",
			"properties": {
				"image": "egolden/training-indices:latest"
			}
		}
    ]
}
```

## step 6) register and test your task within a workflow using gbdxtools
(navigate to directory containing JSON task definition, then register using the gbdxtools command `gbdx.task_registry.register(json_filename = 'hello-gbdx-definition.json')`

(Delete your task from GBDX) `gbdx.task_registry.delete(<task-name>)`

# (TO DOs)
- [X]purpose of tutorial, assumtions about user knowledge before starting this tutorial, link to pre-reqs, etc
- [X]change script so image and shapefile input diff directory
- add string input to script and task definition
- images to folder with hyperlinks
  - diagrams (how platform orchestrates data movement and processing using AWS and Docker)
  - docker hub (crop image first)
  - naming conventions consistency
- [X]use os library to write i/o
- [X]create output directory to write out masked tif
- [X]add short explanations/intro for each segment
- expand/clarify section intros and improve titles (adjust TOC links)
- [X]keep commented out lines?
- add more docker hub screen shots
- fix Dockerfile (check libraries)(docker hub first? build without naming?)
- add image showing navigation within Docker container ('exit', right?)
- show how test script within Docker container 
- [X]add push instructions
- [X]fix JSON script (include required versioning)
- write i/o cheatsheet/diagram (highlighted text?)
- add test files (test the test files)
- explain to download/upload test files to s3
- [X]add TOC hyperlinks 
- add TOP anchors
- add remove container command to run container command (docker run --rm image_name)[doc here](https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes)
