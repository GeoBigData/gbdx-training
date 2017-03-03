from gbdxtools import Interface
gbdx = Interface()

# build the source buckets for the image and the shapefile
gbdx_info = gbdx.s3.info
ntt_bucket = "s3://" + gbdx_info['bucket'] + "/" + gbdx_info['prefix']
image_source_path = ntt_bucket + "/ntt_training_data"
shp_source_path = ntt_bucket + "/ntt_training_data_shp"

# create the target path
target_path = "DL_output"

# declare the clip task with input ports
ntt_task = gbdx.Task("clip_raster_DL",input_image=image_source_path,input_shapefile=shp_source_path)

# define the workflow and output data location
workflow = gbdx.Workflow([ntt_task])
workflow.savedata(ntt_task.outputs.data_out,location=target_path)

# execute the workflow and return the workflow id/status
workflow.execute()
print(workflow.id)
print(workflow.status)