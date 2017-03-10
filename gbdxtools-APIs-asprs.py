import sys
import json
print (sys.executable)
# print (sys.version)

# Next, we import GBDXTools and provide that library our credentials
# Note, this is well documented here: http://gbdxtools.readthedocs.io/en/latest/
# Also note that the credentials are available here: https://gbdx.geobigdata.io/

import gbdxtools
gbdx = gbdxtools.Interface(username='getdano@gmail.com',
    password='ix8S3YM5PCdW',
    client_id='!GT-S!uCTjq;fpq08N2m35f7S@2?JLrR4hw=JIRU',
    client_secret='wR?XFMyYD=o70KU3GA8F4Z7Q.n938YIYCJbT8ypD;LbEql_jB?B@V9hb!G9SZXnA.6cJIqt!8b2dxAYJqLp?_H;NmQX;xAQH.C9fyBA5xIn0IMVd1gPJfHEo_smo.VuO')

# We use the JSON library to print the GBDX Tools object, which has some useful information
print json.dumps(gbdx.s3.info, sort_keys=True, indent=4, separators=(',', ': '))


# Now we can test to make sure that GBDXTOols is working and we have access to the API
# If everything worked, you should see a list of tasks that can be run on GBDX

# Use GBDXTools to get the list of tasks
raw_task_list = gbdx.gbdx_connection.get("https://geobigdata.io/workflows/v1/tasks")

# The text needs to be converted to JSON for access and display
task_list = raw_task_list.json()

print json.dumps(task_list, sort_keys=True, indent=4, separators=(',', ': '))



# Search the catalog
# We will walk through this in a few steps
# First, we will search using a geographic area (note that this is the same one we used earlier...)

wkt_string = "POLYGON((151.247484595670215 -33.956915138583831, 151.247484595670215 -33.941147704639356, 151.266492160171651 -33.941147704639356, 151.266492160171651 -33.956915138583831,151.247484595670215 -33.956915138583831))"
results = gbdx.catalog.search(searchAreaWkt=wkt_string)
print len(results)
# print json.dumps(results[0:10], sort_keys=True, indent=4, separators=(',', ': '))


# Now we filter by the date range
results = gbdx.catalog.search(searchAreaWkt=wkt_string,
                              startDate="2016-09-08T00:00:00.000Z",
                              endDate="2017-03-08T23:59:59.999Z")
print len(results)
# print json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))

# Last, we filter by the image metadata
# At this point, we have the same filters we specified earlier in the web interface


filters = [
        "cloudCover < 10",
        "offNadirAngle < 15",
        "imageBands = 'Pan_MS1_MS2'"
]

results = gbdx.catalog.search(searchAreaWkt=wkt_string,
                              startDate="2016-09-08T00:00:00.000Z",
                              endDate="2017-03-08T23:59:59.999Z",
                              filters=filters)
# print len(results)
print json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))


# Now that we have an image, we can get the full metadata using the CatID

record = gbdx.catalog.get('10400100245B7800')

print json.dumps(record, sort_keys=True, indent=4, separators=(',', ': '))

# One important piece of information is the location of the image on S3

s3path = gbdx.catalog.get_data_location(catalog_id='10400100245B7800')

print s3path


# Ordering API: Imagery to AWS S3
# It is important to consider whether the image is available for processing on S3. If not, it has to be ordered.

cat_ids = ['10400100245B7800']

# Let's check the status of this CatID

order_id = gbdx.ordering.order(cat_ids)
order_status = gbdx.ordering.status(order_id)

print json.dumps(order_status, sort_keys=True, indent=4, separators=(',', ': '))


# We can see above that this image is delivered, which means it is available on S3

# Get detailed information about task inputs and outputs

task = gbdx.Task("AOP_Strip_Processor")
print json.dumps(task.definition, sort_keys=True, indent=4, separators=(',', ': '))

print task.inputs

print task.inputs.enable_acomp

print task.outputs

print task.outputs.data

# Creating a Workflow to run a Task
# A "workflow" is a series of tasks chained together to run on the GBDX platform.
# Each "task" is an individual process that performs a specific action against data, of which the inputs and outputs must be through S3.
# The outputs of one task are frequently the inputs to another.
# S3 inputs and outputs
# Assign the S3 location of input imagery via its Catalog ID metadata that we obtained previously

print s3path

# We can use this location as the input for our task
# We also set the output location as the subdirectory of our bucket where we want the results to be sent.

source_s3 = "s3://receiving-dgcs-tdgplatform-com/056244928010_01_003"
target_s3 = "gbdx_training_gbdxtools/10400100245B7800/acomped"

# Defining The workflow tasks
# The recommended first task to assign in any workflow is the Advanced Image Preprocessor Task, which can orthorectify, atmospherically compensate, and/or pansharpen imagery

aoptask = gbdx.Task("AOP_Strip_Processor", data=source_s3, enable_acomp=True, enable_pansharpen=False, enable_dra=False)
workflow = gbdx.Workflow([ aoptask ])

# We can ensure that the output is sent to our S3 bucket by specifying the savedata parameter

workflow.savedata(aoptask.outputs.data, location=target_s3)

# The final step is to add the task to the workflow and execute

wf_def = workflow.generate_workflow_description()
print json.dumps(wf_def, sort_keys=True, indent=4, separators=(',', ': '))

workflow.execute()

# We can use the workflow id to track and manage workflows

print workflow.id

# Tracking the status for example

print json.dumps(workflow.status, sort_keys=True, indent=4, separators=(',', ': '))

# Detailed status is available as the workflow events

print json.dumps(workflow.events, sort_keys=True, indent=4, separators=(',', ': '))

# Creating a more complex Workflow by Chaining Multiple Tasks Together
# Let's say we want to clip the raster once we have pre-processed it
# Note, this will not actually run as the cliptask hasn't been created yet...

some_shp_file = "s3://gbd-customer-data/6bb1a2e6-7941-4307-8739-349dc22e7f41/a_shape_file/clip_file.shp"
target_s3_2 = "gbdx_training_gbdxtools/10400100245B7800/acomped_and_clipped"

aoptask = gbdx.Task("AOP_Strip_Processor", data=source_s3, enable_acomp=True, enable_pansharpen=False, enable_dra=False)

cliptask = gbdx.Task('clip_raster', input_image=aoptask.outputs.data.value, input_shapefile=some_shp_file)

workflow_2 = gbdx.Workflow([ aoptask, cliptask ])

workflow_2.savedata(cliptask.outputs.data, location=target_s3_2)

wf_def = workflow.generate_workflow_description()
print json.dumps(wf_def, sort_keys=True, indent=4, separators=(',', ': '))

# workflow.execute()

