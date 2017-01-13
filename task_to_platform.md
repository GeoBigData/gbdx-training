# (TO DOs)
- purpose of tutorial, assumtions about user knowledge before starting this tutorial, link to pre-reqs, etc
  - gbdxtools
- change script so image and shapefile input diff directory
- add string input to script and task definition
- images to folder with hyperlinks
  - diagrams (how platform orchestrates data movement and processing using AWS and Docker)
  - docker hub (crop image first)
  - naming conventions consistency
- [X]use os library to write i/o
- [X]create output directory to write out masked tif
- expand/clarify section intros
- add short explanations/intro for each segment
- [X]keep commented out lines?
- fix Dockerfile (check libraries)(docker hub first? build without naming?)
- show how test script within Docker container 
- add push instructions
- fix JSON script (include required versioning)
- write i/o cheatsheet/diagram (highlighted text?)
- add test files (test the test files)
- explain to upload test files to s3
- add TOC hyperlinks 
- troubleshooting? (Dockerfile extension)
## this tutorial.. 
- demonstrates how to put a very simple task on the platform, from start to finish 
- presumes user has a gbdx account, has installed gbdxtools including config file, has installed docker, registered for a Docker Hub account, and is familiar with python
- has previous exposure to AWS, Docker, and GBDX APIs concepts (workflow, tasks, etc..)

(TOC)
[step 1) write and test algorithm that processes locally](#test test) 


(placeholder for diagram of platform architecture)
- platform orchestrates movement and processing of data within AWS
- data is stored in AWS S3, processing happens in AWS EC2s
- by placing your algorithm within a Docker and registering the image on Docker Hub, the platform is able to retrieve, build, and execute your algorithm within the Workflow system
- you can then process data in concert with other data and algorithms to execute an entire workflow

## step 1) write and test algorithm that processes locally 
here is an example python script that clips a raster image using a shapefile (need to explain how)
  ```python
  import fiona
  import rasterio
  import os
  import glob

  in_path = os.path.join(os.path.expanduser('~'), 'documents', 'demo', 'input')
  ward_shape = glob.glob(in_path + '/*.shp')
  ward_image = glob.glob(in_path + '/*.tif')
  
  out_path = os.path.join(os.path.expanduser('~'), 'documents', 'demo', 'output')
  os.chdir(out_path)
  
  with fiona.open(shapefile, "r") as shapefile:
      features = [feature["geometry"] for feature in shapefile]

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

## step 2) modify to match I/O structure within Docker container
(short explanation about platform orchestrating data movement within docker container and i/o naming conventions)
  ```python
  import fiona
  import rasterio
  import os
  import glob

  # in_path = os.path.join(os.path.expanduser('~'), 'documents', 'demo', 'input')
  in_path = '/mnt/work/input/data_in'
  ward_shape = glob.glob(in_path + '/*.shp')
  ward_image = glob.glob(in_path + '/*.tif')
  
  # out_path = os.path.join(os.path.expanduser('~'), 'documents', 'demo', 'output')
  out_path = '/mnt/work/output/data_out'
  os.chdir(out_path)
  
  with fiona.open(shapefile, "r") as shapefile:
      features = [feature["geometry"] for feature in shapefile]

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
## TEST test

## step 3) prepare Docker Hub repository
(short explanation about how platform uses Docker Hub, sign up, log in, create repository, add platform collaborators: tdgpbuild, tdgpdeploy, tdgplatform) [screenshot](screenshots/add_collaborators.png)<a href="http://example.com/" target="_blank">example</a>
![alt tag](https://cloud.githubusercontent.com/assets/9055899/21915498/79db2586-d8f7-11e6-9b0a-91ec51740f30.png)

## step 4) write, build, test, push build Dockerfile 
(explantion about why, what it does, best practices, etc)
  ```
  FROM ubuntu:14.04
  RUN apt-get update && apt-get -y install\
    python \
    vim\
    build-essential\
    python-software-properties\
    software-properties-common\
    python-pip\
    python-dev
  RUN mkdir /
  ADD ./bin /training-indices
  CMD python /training-indices/mud_water_indices.py
  ```
Docker command to build container `docker build -t <docker username>/<docker repository> .` (note '.' at end of command)
Look at your images `docker images`
Docker command to run container with mounted data for testing `docker run -v ~/<full path to input data>:/mnt/work/input -it <docker username>/<docker repository> bash`

## step 5) write JSON task definition 
(will need to write a JSON doc with a task definition, then use task registery API to register to platform)
```json
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
