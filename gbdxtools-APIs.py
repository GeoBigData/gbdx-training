
# coding: utf-8

# # Intro
# 
# DigitalGlobe's GBDX platform provides customers with a fast and easy way to search, order, and process images and their data. This tutorial is intended to demonstrate how to access GBDX APIs via the Python SDK, gbdxtools. Specifically, this tutorial will cover:
# 
# 1. [Setup gbdxtools](#1.-Setup-gbdxtools)
# 2. [Catalog API](#2.-Catalog-API)
# 3. [Ordering API](#3.-Ordering-API)
# 4. [Workflow API](#4.-Workflow-API)
# 5. [Manage Workflows](#5.-Manage-Workflows)
# 6. [A more complex Workflow](#6.-A-more-complex-Workflow)

# ## 1. Setup gbdxtools
# Gbdxtools provides an easy Python interface to GBDX APIs. A pre-requisite for this tutorial is to install gbdxtools. Instructions for doing so can be found at https://github.com/GeoBigData/gbdx-training. These instructions also explain how to create a config file that provides your GBDX credentials to the gbdxtools library. If you haven't set up that config file, however, we'll show you how to explicitly pass in your GBDX credentials.
# 
# __1.1 After you install gbdxtools, you need to import gbdxtools and initiate the Interface object that handles GBDX authentication.__ 
# 
# __*If you have successfully set up your ~.gbdx-config file*, run the code in the following cell to instantiate a gbdxtools session.__

# In[ ]:

from gbdxtools import Interface
gbdx = Interface()


# __*If you don't have a working ~.gbdx-config file*, you will need to fill in your your GBDX username, password, Client ID and Client Secret before running the code in the following cell. This information can be found under your Profile information at https://gbdx.geobigdata.io/profile __ 

# In[ ]:

import gbdxtools
gbdx = gbdxtools.Interface(
    username='',
    password='',
    client_id='',
    client_secret='')


# __1.2 Now that you've imported gbdxtools and authenticated your credentials, we need to you import a couple more libraries. Import the '`sys`' library so you can check your Python instance, and '`json`' so you can print output in an easy to read format. The print statement will return your Python instance.__ 

# In[ ]:

import sys
import json
print (sys.executable)


# ## 2. Catalog API

# The Catalog API is the backbone of data discovery through the APIs and allows you to search the all of the records and metadata contained in the DigitalGlobe archive, by geographic area, or parameters such as acquisition data, sensor, cloud cover, etc.
# 
# __2.1 First, search the catalog by geographic area, as defined by a WKT polygon. All imagery that intersects the polygon will be returned, but we'll just look at one result.__ 

# In[ ]:

wkt_string = "POLYGON((151.247484595670215 -33.956915138583831, 151.247484595670215 -33.941147704639356, 151.266492160171651 -33.941147704639356, 151.266492160171651 -33.956915138583831,151.247484595670215 -33.956915138583831))"

results = gbdx.catalog.search(searchAreaWkt=wkt_string)
print json.dumps(results[15], sort_keys=True, indent=4, separators=(',', ': '))


# There is a lot of interesting information here, such as image bands, image resolution, cloud cover, timestamp, etc. If you would like to learn more about the image metadata, check the documentation at   http://gbdxdocs.digitalglobe.com/docs/catalog-v2-record-metadata.
# 
# One key metadata value to note is the Catalog ID of the image, which is unique to that image. When you order imagery to GBDX, you'll need to order it via its Catalog ID. 
# 
# ```json
# "catalogID": "10400100290BFF00",
# ```

# __2.2 Add a start and end date to your search to filter the results by date range, compare the number of filtered results to the original search results.__ 

# In[ ]:

print len(results)


# In[ ]:

results = gbdx.catalog.search(searchAreaWkt=wkt_string,
                              startDate="2016-09-08T00:00:00.000Z",
                              endDate="2017-03-08T23:59:59.999Z")
print len(results)


# __2.3 Last, filter your search results by specific metadata values. Add filters for cloud cover, off-nadir angle, and image bands, and look at the results.__ 

# In[ ]:

filters = [
        "cloudCover < 10",
        "offNadirAngle < 15",
        "imageBands = 'Pan_MS1_MS2'"
]

results = gbdx.catalog.search(searchAreaWkt=wkt_string,
                              startDate="2016-09-08T00:00:00.000Z",
                              endDate="2017-03-08T23:59:59.999Z",
                              filters=filters)
print len(results)


# In[ ]:

print json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))


# __ 2.4 Given the Catalog ID for an image, fetch its metadata.__

# In[ ]:

record = gbdx.catalog.get('10400100245B7800')
print json.dumps(record, sort_keys=True, indent=4, separators=(',', ': '))


# __2.5 Given the Catalog ID for an image, return the WKT for the image strip footprint.__

# In[ ]:

record_wkt = gbdx.catalog.get_strip_footprint_wkt('10400100245B7800')
print json.dumps(record_wkt, sort_keys=True, indent=4, separators=(',', ': '))


# __ 2.6 When an image is ordered to GBDX, it will be pushed an S3 bucket on AWS. Given the Catalog ID for an image, get its S3 location.__

# In[ ]:

s3path = gbdx.catalog.get_data_location(catalog_id='10400100245B7800')
print s3path


# ## 3. Ordering API

# Imagery will often need to first be ordered to GBDX before it can be processed. The GBDX Orders API lets you order imagery by catalog ID and check the status of your order. Learn more about Ordering at http://gbdxdocs.digitalglobe.com/docs/ordering-course-v2.
# 
# __ 3.1 Define the Catalog ID to be ordered.__

# In[ ]:

cat_ids = ['10400100245B7800']


# It is important to consider whether the image is available for processing on S3. If not, it must be ordered. In the following code, we will order an image by its catalog ID, which will return an order ID. We can then use that Order ID to check the status of the order, whether it's delivered and its S3 location.  

# __ 3.2 Order the image by its Catalog ID, return and print the order status. Because this image has already been ordered to GBDX, its 'state' is 'delivered' and the status call returns its location on S3.__

# In[ ]:

order_id = gbdx.ordering.order(cat_ids)
order_status = gbdx.ordering.status(order_id)

print json.dumps(order_status, sort_keys=True, indent=4, separators=(',', ': '))


# __ 3.3 You can order several catalog IDs in this way, up to 100. Use the same format as above to order three Catalog IDs.__

# In[ ]:

cat_ids = ['101001000350E300', '1040010014816F00', '10400100245B7800']


# In[ ]:

order_id = gbdx.ordering.order(cat_ids)
order_status = gbdx.ordering.status(order_id)

print json.dumps(order_status, sort_keys=True, indent=4, separators=(',', ': '))


# ## 4. Workflow API

# A "workflow" is a series of tasks chained together to run on the GBDX platform. Each "task" is an individual process that performs a specific action against data, of which the inputs and outputs must be through S3. The outputs of one task are frequently the inputs to another.  

# ### Tasks

# The first step to building a Workflow is to set up the individual Tasks that make up the Workflow. Each Task needs to be defined with its registered Task name, and assigned inputs. You can find documentation on many of the Tasks you'll use under 'Certified Algorithms' at http://gbdxdocs.digitalglobe.com/docs. However, it is also easy to interact with the Task object to get more information about it. 
# 
# The first Task in almost any Workflow is the Advanced Image Processor Task, which orthorectifies raw imagery and offers other image pre-processing options. Documentation at https://gbdxdocs.digitalglobe.com/docs/advanced-image-preprocessor.
# 
# __4.1 Define the Advanced Image Preprocessor task using its registered Task name, 'AOP_Strip_Processor', and print out the task definition.__

# In[ ]:

aop_task = gbdx.Task("AOP_Strip_Processor")
print json.dumps(aop_task.definition, sort_keys=True, indent=2, separators=(',', ': '))


# The Task definition has a lot of useful information, including descriptions of inputs and outputs, and which of the inputs are required.
# 
# __ 4.2 Run the code in the following cell to get a list of inputs for this Task.__ 

# In[ ]:

print aop_task.inputs


# __ 4.3 Append an input port name to the same call to get detailed information about that input.__

# In[ ]:

print aop_task.inputs.enable_acomp


# __ 4.4 Run the following code cells to find out more information about the Task outputs.__ 

# In[ ]:

aop_task.outputs


# In[ ]:

aop_task.outputs.data


# ___
# Now that you know about Tasks, and about inputs and outputs to a Task, let's walk through the steps to building a Workflow. You will get a chance to try it out at the end of this explanation.  
# 
# __S3 inputs and outputs__
# 
# The input data for a Task must be located on S3. This could be in the way of an image that you've ordered to GBDX, it could be data that you've staged in your S3 bucket, or it could be the output from a previous Task in the Workflow. For this example Workflow, you're going to use an image ordered to GBDX as input to the Task. 
# 
# > Define the input data source for your Workflow by getting the S3 location of an image, via its Catalog ID.
# 
# ```python
# source_s3 = gbdx.catalog.get_data_location(catalog_id='10400100245B7800')
# ```

# Just as the input must come from an S3 location, the output of a Task must be saved to an S3 location. Gbdxtools has a 'savedata' feature that will automatically save the output to your Customer S3 bucket, under the directory that you specify. We will cover the 'savedata' feature later in the script.
# 
# >Define an output directory. 
# 
# ```python
# target_s3 = 'demo_output/aop_10400100245B7800/'
# ```

# __Defining Task(s) __
# 
# As we mentioned before, the recommended first Task in any Workflow is the Advanced Image Preprocessor Task. Now when you set up this Task to be used in a Workflow, you will pass in the S3 location of the ordered image to its input port called, 'data'.  
# 
# >Define the Advanced Image Preprocessor Task using its Task name, 'AOP_Strip_Processor', and the S3 location of the ordered image as the Task's input.
# 
# ```python
# aop_task = gbdx.Task('AOP_Strip_Processor', data=source_s3)
# ```

# __Assigning Tasks(s) to a Workflow.__
# 
# A Workflow can execute many Tasks and facilitate the movement of data between those Tasks. For this simple example, there is only one Task. 
# 
# > Create a Workflow using the following call, passing in the 'aop_task'.
# 
# ```python
# my_workflow = gbdx.Workflow([ aop_task ])
# ```

# __Starting and saving a Workflow__
# 
# The 'savedata' feature will automatically save the output of this Worflow to your GBDX Customer S3 bucket, to the output directory you defined earlier. 
# 
# > Pass in the output of the 'aop_task', by referencing its output port, which is called 'data'. Set the 'location' parameter of this 'savedata' feature to your defined output directory.
# 
# ```python
# my_workflow.savedata(aop_task.outputs.data, location=target_s3)
# ```
# 
# > Execute the Workflow. Once the Workflow is started, the Platform will spin up the compute resources and data to run each Task, and will run until each of the Tasks in the Workflow has completed. 
# 
# ```python
# my_workflow.execute()
# ```
# 
# >Print and save the Workflow ID, as this will allow you to track and manage your Workflows. 
# 
# ```python
# print my_workflow.id
# ```

# __ 4.5 Run the code in the following cell to execute the Workflow. __

# In[ ]:

# define the S3 location of the input data
source_s3 = gbdx.catalog.get_data_location(catalog_id='10400100245B7800')

# define the S3 location of the output directory
target_s3 = 'demo_output/aop_10400100245B7800/'

# define the pre-processing Task
aop_task = gbdx.Task('AOP_Strip_Processor', data=source_s3)

# define the Workflow
my_workflow = gbdx.Workflow([ aop_task ])

# save the output of the Workflow to S3
my_workflow.savedata(aop_task.outputs.data, location=target_s3)

# execute the Workflow
my_workflow.execute()
print my_workflow.id


# ## 5. Manage Workflows

# Once a Workflow is started, you can use the workflow object, in this case called 'my_workflow', to track and manage it. As long as you have the Workflow ID, you can always access this information. 
# 
# __ 5.1 Get the status of the Workflow. This will return the status of whichever event is currently running within the Workflow. __

# In[ ]:

print my_workflow.status


# __ 5.2 List the events that have taken place or is currently taking place within the Workflow. __

# In[ ]:

print json.dumps(my_workflow.events, sort_keys=True, indent=2, separators=(',', ': '))


# In[ ]:

wf.events


# __ 5.3 Get the stdout and stderr for the Workflow. __

# In[ ]:

my_workflow.stdout


# In[ ]:

my_workflow.stderr


# __ 5.3 Each Task also has a unique ID. Get the Task IDs. __

# In[ ]:

task_ids = my_workflow.task_ids
print task_ids


# __ 5.4 Get the stdout and stderr of a specific Task within the Workflow. __

# In[ ]:

stdout = gbdx.workflow.get_stdout(my_workflow.id, task_ids[0])
print stdout


# In[ ]:

stderr = gbdx.workflow.get_stderr(my_workflow.id, task_ids[0])
print stdout


# __ 5.5 Find out if the Workflow completed and succeeded. __ 

# In[ ]:

my_workflow.complete


# In[ ]:

my_workflow.succeeded


# __ 5.6 Generate the Workflow JSON schema running behind the scenes. __

# In[ ]:

my_workflow.generate_workflow_description()


# You can cancel a Workflow while it's running.
# ```python
# my_workflow.cancel()
# ```

# __ 5.7 You can also get information about your Workflow later if you've saved the Workflow ID. Replace the Workflow ID in the following call with your Workflow ID. __

# In[ ]:

gbdx.workflow.get('4578270231173558359')


# ## 6. A more complex Workflow 

# The above example Workflow only has one Task assigned to it. The power of the Workflow system, however, is in being able to link the output of one Task as input to another Task. In this next example, we will assign the output of the image pre-processing Task as input to a Land Use Land Cover Task (LULC). 
# 
# The LULC Task requires one TIF as input. The output of the image pre-processing Task, however, includes other files in addition to the output TIF. We are going to use the 'gdal-cli' Task, which is a Task that allows you to use GDAL commands as you would in the command line, to pull out just the processed TIF from the image pre-processing output.  
# 
# > You're going to first duplicate what we did in the above example - define the S3 image input and the output directory.
# 
# ```python
# # define the S3 location of the input data
# source_s3 = gbdx.catalog.get_data_location(catalog_id='10400100245B7800')
# 
# # define a directory in which to save the LULC Workflow output
# target_s3 = "egolden/demo_lulc_10400100245B7800/"
# ```

# You're going to use the Advanced Image Preprocessor Task again, but this time you're not going to use just the default parameters. The LULC Task requires multi-spectral, atmospherically compensated imagery that has not been pansharpened or had DRA applied to it. You will need to set the pre-processing Task parameters accordingly.
# 
# > Define the image pre-processing Task, using the S3 location of the ordered image as input, with the parameters needed to prepare imagery for the LULC Task.
# 
# ```python
# aop_task = gbdx.Task('AOP_Strip_Processor', data=source_s3, bands='MS', enable_acomp=True, 
#     enable_pansharpen=False, enable_dra=False)
# ```

# Next, we define the intermediate Task that extracts just the output TIF from 'aop_task'. We'll call it 'glue_task'. This Task's input port has been named, 'data', and you can assign the output from the aop_task to this input port by referencing '`aop_task.outputs.data.value`'.
# 
# > Define the 'glue_task', assigning the aop_task output as the 'glue_task' input. The rest of the command simply moves the TIF to the root of the 'glue_task' output directory, where the next Task can find it. 
# 
# ```python
# glue_task = gbdx.Task('gdal-cli', data=aop_task.outputs.data.value, execution_strategy='runonce',
#     command="""mv $indir/*/*.tif $outdir/""")
# ```

# Now you can define the LULC Task and assign the 'glue_task' output to the LULC Task input, by referencing '`glue_task.outputs.data.value`'. You'll notice that the input port to the LULC Task is called 'raster'. 
# 
# > Define the LULC Task using its registered Task name and passing in the 'glue_task' output. 
# 
# ```python
# lulc_task = gbdx.Task("protogenV2LULC", raster=glue_task.outputs.data.value)
# ```

# The next step is to create a Workflow as you did before, but this time the Workflow will contain more Tasks, with connected inputs and outputs. 
# 
# > Create a Workflow and pass in aop_task, glue_task, and lulc_task.
# 
# ```python
# my_workflow2 = gbdx.Workflow([ aop_task, glue_task, lulc_task ])
# ```

# Use the savedata feature again to save the Workflow output to your GBDX customer S3 bucket, but specify the output of the LULC Task this time. 
# 
# > Specify the output directory for the LULC output. 
# 
# ```python
# my_workflow2.savedata(lulc_task.outputs.data, location=target_s3)
# ```

# > Execute the Workflow, print and save the Workflow ID.
# 
# ```python
# my_workflow2.execute()
# print my_workflow2.id
# ```

# __ 6.1 Run the code in the following cell to execute the new Workflow. __

# In[ ]:

# define the S3 location of the input data
source_s3 = gbdx.catalog.get_data_location(catalog_id='10400100245B7800')

# define a directory in which to save the LULC Workflow output
target_s3 = "egolden/demo_lulc_10400100245B7800/"

# define the pre-processing Task to prepare an image for the LULC Task
aop_task = gbdx.Task('AOP_Strip_Processor', data=source_s3, bands='MS', enable_acomp=True, 
    enable_pansharpen=False, enable_dra=False)

# define the glue Task that grabs just the TIF from aop_task output
glue_task = gbdx.Task('gdal-cli', data=aop_task.outputs.data.value, execution_strategy='runonce',
    command="""mv $indir/*/*.tif $outdir/""")

# define the LULC Task
lulc_task = gbdx.Task("protogenV2LULC", raster=glue_task.outputs.data.value)

# define the Workflow
my_workflow2 = gbdx.Workflow([ aop_task, glue_task, lulc_task ])
                              
# save the LULC output to S3                              
my_workflow2.savedata(lulc_task.outputs.data, location=target_s3)       

# execute the Workflow and print the Workflow ID                              
my_workflow2.execute()
print my_workflow2.id                              


# __ 6.2 Use the tools we learned earlier to track the Workflow. You'll notice that you'll get an event for each Task, for each change in state.__

# In[ ]:

print my_workflow2.status


# In[ ]:

print json.dumps(my_workflow2.events, sort_keys=True, indent=2, separators=(',', ': '))


# In[ ]:

for event in my_workflow2.events:
    print event['task'], event['event']


# # Conclusion
# 
# Congratulations on learning how to search the Catalog, order imagery, and run Workflows. You can see the output of your Workflows by logging into the [S3 browser](http://s3browser.geobigdata.io/) with your GBDX credentials, and navigating the output directories you created at 'demo_output/'. 
