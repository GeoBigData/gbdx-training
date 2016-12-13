
# First, initialize the Interface object that handles authentication
from gbdxtools import Interface
gbdx = Interface()

# Catalog API: Search the DigitalGlobe archive

# Search the catalog by geographic area
wkt_string = "POLYGON((-122.43434482199342028 47.69012820633496119,-122.24650297391180231 47.6831711008504584,-122.23954586842728531 47.49532925276882622,-122.41347350553991191 47.49532925276882622,-122.43434482199342028 47.69012820633496119))"
results = gbdx.catalog.search(searchAreaWkt=wkt_string)
print results[0:10]

# Filter by date
results = gbdx.catalog.search(searchAreaWkt=wkt_string,
                              startDate="2015-12-09T00:00:00.000Z",
                              endDate="2016-12-09T00:00:00.000Z")
print results

# Can specify DigitalGlobe or Landsat sensor
types = [ "DigitalGlobeAcquisition"]
results = gbdx.catalog.search(searchAreaWkt=wkt_string,
                              startDate="2015-12-09T00:00:00.000Z",
                              endDate="2016-12-09T00:00:00.000Z",
                              types=types)
print results

# Filter results by catalog properties
filters = [
        "(sensorPlatformName = 'WORLDVIEW01' OR sensorPlatformName ='WORLDVIEW02')",
        "cloudCover < 10",
        "offNadirAngle > 10"
]

results = gbdx.catalog.search(searchAreaWkt=wkt_string,
                              startDate="2015-12-09T00:00:00.000Z",
                              endDate="2016-12-09T00:00:00.000Z",
                              types=types,
                              filters=filters)
print results

# Get metadata Info about a given Catalog ID
record = gbdx.catalog.get('1050410011360700')
print record

# Find data location given a Catalog ID
s3path = gbdx.catalog.get_data_location(catalog_id='1030010045539700')
print s3path

# Ordering API: Imagery to AWS S3
cat_ids = ['10400100143FC900']

order_id = gbdx.ordering.order(cat_ids)
order_status = gbdx.ordering.status(order_id)

print order_status

cat_ids = ['103001005B38CE00', '103001005B078B00']

order_id = gbdx.ordering.order(cat_ids)
order_status = gbdx.ordering.status(order_id)

print order_status

'''
Workflow API: String together tasks and analyses on imagery and other data
A "workflow" is a series of tasks chained together to run on the GBDX platform. Each "task" is an individual process that performs a specific action against data, of which the inputs and outputs must be through S3. The outputs of one task are frequently the inputs to another.
'''

# S3 inputs and outputs

# Assign the S3 location of input imagery via its Catalog ID metadata
source_s3 = gbdx.catalog.get_data_location(catalog_id='103001005B38CE00')
print source_s3

# Assign the output S3 location to the private S3 bucket included with your GBDX account. Access your bucket name and prefix via your S3 credentials
s3creds = gbdx.s3.info
print s3creds

bucket = s3creds['bucket']
prefix = s3creds['prefix']
target_s3 = "s3://" + bucket + "/" + prefix + "/" + "demo_output/"
print target_s3

# The workflow

# The recommended first task to assign in any workflow is the Advanced Image Preprocessor Task, which can orthorectify, atmospherically compensate, and/or pansharpen imagery 
aop_task = aop_task = gbdx.Task('AOP_Strip_Processor', data=source_s3)

# Every workflow must finish with a task that saves the output to a S3 location
s3_task = gbdx.Task('StageDataToS3', data=aop_task.outputs.data.value, destination=target_s3)

# Chain the assigned tasks into a workflow and execute
workflow = gbdx.Workflow([ aop_task, s3_task ])
workflow.execute()

# Track and manage workflows
workflow.id
workflow.status
workflow.cancel()

# Putting together a more complex workflow

# Assign the Automated Land Cover Classification task, which in this case requires a prep task to pull just the imagery from the output of the Advanced Image Preprocessor
glue_task = gbdx.Task('gdal-cli', data=aop_task.outputs.data.value, execution_strategy='runonce',
                         command="""mv $indir/*/*.tif $outdir/""")
lulc_task = gbdx.Task("protogenV2LULC", raster=glue_task.outputs.data.value)
workflow = gbdx.Workflow([ aop_task, glue_task, lulc_task, s3_task ])
workflow.execute()

# Get detailed information about task inputs and outputs
task = gbdx.Task("AOP_Strip_Processor")
print task.inputs
print task.inputs.enable_acomp
print task.outputs
print task.outputs.data