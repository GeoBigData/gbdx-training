# initiate the Interface object that handles GBDX authentification
from gbdxtools import Interface
gbdx = Interface()

# define the S3 path for an image by passing in its Catalog ID 
source_s3 = gbdx.catalog.get_data_location(catalog_id='10400100245B7800')

# define an input shapefile from S3
shape_path = 's3://tutorial-files/this_shp_will_clip_10400100245B7800/'

# define the 'AOP_Strip_Processor' 
aop_task = gbdx.Task('AOP_Strip_Processor', data=source_s3, enable_pansharpen=True)

# define the 'gdal_cli' Task
glue_task = gbdx.Task('gdal-cli', data=aop_task.outputs.data.value, execution_strategy='runonce',
                         command="""mv $indir/*/*.tif $outdir/""")

# define the 'clip_raster' Task 
clip_task = gbdx.Task("clip_raster_gt", input_raster=glue_task.outputs.data.value, input_shapefile=shape_path)

# build a Workflow to run the 'clip_raster' Task
workflow= gbdx.Workflow([aop_task, glue_task, clip_task])

# specify where to save the output within your customer bucket
workflow.savedata(clip_task.outputs.data_out, location='task_demo/clip_raster')

# kick off the Workflow and keep track of the Workflow ID
workflow.execute()
print workflow.id
