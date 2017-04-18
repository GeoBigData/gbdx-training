# GBDX APIs

## GBDX Web App demo
The GBDX web application allows users to easily interact with the GBDX APIs in a GUI (graphical user interface). You can search, filter and select imagery from the DigitalGlobe archive to add to a project. You can then select from a library of tasks, or analytic processes, to run against the imagery. You can then track your progress and go to your results. 

- AOIs - define an area of interest
- METADATA - important image properties 
- FILTER and select imagery
- TASK, add a task
- RUN a project
- STATUS - check your progress
- RESULTS - find  your output

__Web App__
-  https://gbdx.geobigdata.io
-  http://s3browser.geobigdata.io
-  http://gbdxdocs.digitalglobe.com/docs/web-application-course

## Catalog API
The Catalog API is the backbone of data discovery through the APIs and contains all of the records and metadata that can be searched. It allows you to seach the entire DigitalGlobe archive and set parameters such as coordinates and search filters to find exactly the data you need.

- SEARCH imagery by WKT string
- FILTER imagery by properties 
- GET METADATA from a Catalog ID

__Postman__
- JSON example

__gbxtools__
- Notebook or Python
- http://gbdxtools.readthedocs.io/

## Ordering API
At this time, most of the DigitalGlobe Archive lives on tape in the Factory. An image can be moved from the factory to the platform by “ordering” the image. This process can take a few minutes to a few hours. If the image has been ordered by anyone else in the past, however, the ordering API will simply return the S3 location of that image. 

- ORDER imagery by Catalog ID
- STATUS - check the status of an order
- S3 LOCATION - get the S3 location of delivered imagery

__gbdxtools__
- continuation of gbdxools Notebook/Python

## Workflow API 
The real power of the GBDX platform is the ability to have access to the full catalog of DigitalGlobe data "right next" to the algorithms and compute power needed to extract information from that data.  GBDX Algorithms are called Tasks.  A "Task" is a data processing algorithm that contains well-defined input and output data requirements. Tasks are developed and packaged in Dockers and registered to Docker Hub, where they are available to the Workflow system. 

- TASKS - what it is and how to get more info
- ASSIGN inputs and outputs to a Task
- WORKFLOW - what it is and how to build one
- EXECUTE a Workflow of Tasks
- STATUS - check the status and manage the Workflow

__Postman__
- JSON examples

__gbdxtools__
- continuation of gbdxools Notebook/Python

# Create a Task
Users can and are encouraged to build their own custom analytic capabilities to use on the Platform. This process starts with packaging up the algorithm, along with the libraries and dependencies needed to run it, in a Docker, and pushing it to a Docker Hub repository. You can then register a definition of the Task - the Docker reference, expected inputs and outputs, etc - to the Platform. From there, it is simply a matter of asking the Workflow system to execute your Task, along with any other Tasks, typically via Postman or gbdxtools.    

1. DEVELOP a task
2. MODIFY inputs and outputs 
3. DOCKERFILE - instructions for Docker image
4. BUILD and RUN a Docker
5. PUSH Docker to Docker Hub
6. ADD GBDX collaborators to Docker Hub repository 
7. WRITE JSON Task definition
8. REGISTER Task on Platform
9. WORKFLOW - use your Task in a Workflow

## 1. Develop a Task 
A 'task' starts with the code you've written to perform some desired analysis or function. For this tutorial, we've provided example code for a Task that simply clips a raster to a shapefile. 

- OVERVIEW of what the code is doing

__code editor__
- Python example

## 2. Modify inputs and outputs
When the Platform spins up your Task, it will also load the necessary data into input ports within the Docker that runs your Task. These input ports have standard filepath, `/mnt/work/input`, as do the output ports, `/mnt/work/output`. You will need to modify your Task script to accept input and write output from these filepaths.

- MODIFY script inputs and outputs to match Docker ports

__code editor__
- Python example

## 3. Dockerfile - instructions for Docker image
A Dockerfile is a set of instructions to package up your Task script, along with the libraries and dependencies needed to run that script, into a portable Docker. This means that you could give your Docker to anyone using whatever machine or OS, and they would be able to run the Docker and produce the same, consistent output.

- SET UP a Docker project directory
- WRITE a Dockerfile 

__code editor__
- your local working directory
- Dockerfile example

## 4. Build and run a Docker
From the Dockerfile, you can build, run, and test a Docker

- BUILD a Docker image
- RUN a Docker container
- NAVIGATE within a Docker container

__Docker shell or terminal__ <br/>
- `docker images` <br/>
- `docker build -t <docker username>/<docker repository> .` (note the period at end of this command) <br/>
- `docker run -it <docker username>/<docker repository> bash` <br/>
- `ls`, `cd`, `cd ..`, `cd /`, `exit` <br/>

## 5. Push Docker to Docker Hub
The Platform needs to be able to pull and run your Docker when it's executing your Task. In this exercise, you're going to push your Docker to Docker Hub, using your Docker Hub credentials. 

- LOG IN to Docker Hub from the terminal
- PUSH your Docker to Docker Hub

__Docker shell or terminal__
- `docker login --username <docker username> --password <docker password>`
- `docker push <docker username>/<docker repository>`

## 6. Add GBDX collaborators to Docker Hub repository
Your Docker repository on Docker Hub can be public or private, but certain GBDX collaborators must be added to the repository in order for the Platform to pull and run the Docker. 

- ADD COLLABORATORS

__Docker Hub__
- [Docker Hub](https://hub.docker.com/)
- `tdgpbuild`
- `tdgpdeploy`
- `tdgplatform`

## 7. Write JSON Task definition
You're nearly there! In order for the Platform to recognize and execute your Task properly, you need to register the Task using a JSON Task definition. This definition will include things like owner and description, required inputs and outputs, and importantly, the name of your Docker image. 

- EXPLAIN the pieces of a Task definition
- MODIFY the Task definition JSON for your task

__code editor__
- JSON example

## 8. Register Task on Platform
Now that you have a Task definition ready, you can use the GDBX Register API to register your Task to the Platform. 

- NAVIGATE to your Task definition file in the terminal
- GBDXTOOLS - start Python and a gbdxtools session
- REGISTER Task to Platform using register API

__terminal__
- your local working directory
- Python

```python
from gbdxtools import Interface
gbdx = Interface()

gbdx.task_registry.register(json_filename = 'clip-raster-definition.json')
```

## 9. Workflow - use your Task in a Workflow
You now have your own, custom task that be used on the Platform. This means that you can create a Workflow that incorporates DigitalGlobe Tasks, other people's Tasks, in addition to your custom Task. Final step is to test that the Task works as expected by using it in a Workflow.

- IT'S A TASK! - see your Task in a list of Platform Tasks
- WORKFLOW - connect the inputs/outputs of your Task to other Tasks in a Workflow

__gbdxtools__
- Notebook or Python

