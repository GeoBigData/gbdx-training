from gbdxtools import Interface
gbdx = Interface()

# build the source buckets for the image and the shapefile
gbdx_info = gbdx.s3.info
my_bucket = "s3://" + gbdx_info['bucket'] + "/" + gbdx_info['prefix']
shp_path = my_bucket + "/demo_task_shp"

image_path = gbdx.catalog.get_data_location(catalog_id='10400100245B7800')

# create the target path
target_path = "demo_task_output"

# declare the clip task with input ports
clip_task = gbdx.Task("clip_raster_ESG", input_image=image_path, input_shapefile=shp_path)

# define the workflow and output data location
workflow = gbdx.Workflow([clip_task])
workflow.savedata(clip_task.outputs.data_out,location=target_path)

# execute the workflow and return the workflow id/status
workflow.execute()
print(workflow.id)
print(workflow.status)
