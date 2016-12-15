#!/usr/bin/python

#############################################################################################
#
#  Order-AOP-RasterClip-OpenSkyNet-Workflow.py
#
#  Created by: Beth Stein and Elizabeth Golden
#              DigitalGlobe GBD Solutions
#
#  Version 0.1: December 7, 2016
#               - run OpenSkyNet-v5 using gbdxtools
#
#  Usage: python Order-AOP-RasterClip-OpenSkyNet-Workflow.py 
#
#  This script creates a GBDX workflow that will order images, produce an AOP image, 
#  		clip the image to a shapefile, and run OpenSkyNet-v5.
#
#  
#  The script is dependent on gbdxtools 0.6.7 or greater to function correctly
#
#############################################################################################

# Instantiate gbdxtools
from gbdxtools import Interface
gbdx = Interface()
gbdx_info = gbdx.s3.info

# Build a list of catalog ids for input into workflow
catid = ['10400100234F9700']

# Create the auto order task to place the catid order, or get the current location of the data
order_task = gbdx.Task("Auto_Ordering",cat_id=catid)
order_task.impersonation_allowed = True
data_loc = order_task.outputs.s3_location.value

# Build the AOP task used in the workflow
gsd = "0.5"
aop_task = gbdx.Task("AOP_Strip_Processor", data=data_loc, enable_acomp=True, enable_pansharpen=True, enable_dra=True, ortho_epsg="UTM", ortho_pixel_size=gsd, bands="PAN+MS")
stage_task1 = gbdx.Task("StageDataToS3", data=aop_task.outputs.data.value, destination='s3://gbd-customer-data/58600248-2927-4523-b44b-5fec3d278c09/bstein/test_12-13-16')

# Crop raster task
crop_raster_task = gbdx.Task("RasterClip_Extents", raster=aop_task.outputs.data.value, shp='s3://gbd-customer-data/58600248-2927-4523-b44b-5fec3d278c09/bstein/openskynet/test_12-12-16/', chip_name="055813637010", file_ext="True")
stage_task2 = gbdx.Task("StageDataToS3", data=crop_raster_task.outputs.data.value, destination='s3://gbd-customer-data/58600248-2927-4523-b44b-5fec3d278c09/bstein/test_12-13-16')

# OpenSkyNet-v5 task
openskynet_task = gbdx.Task("openskynet-v5",data=crop_raster_task.outputs.data.value, model_catalog_endpoint="devvector.geobigdata.io", log_level="trace", confidence="0.85", pyramid=True, pyramid_window_sizes="[150, 80]", pyramid_step_sizes="[40, 20]", step_size="15", tags="Airliner, Fighter, Helicopter")
openskynet_task.impersonation_allowed = True
openskynet_task.domain = "nvidiagpu"
stage_task3 = gbdx.Task("StageDataToS3", data=openskynet_task.get_output('results'), destination='s3://gbd-customer-data/58600248-2927-4523-b44b-5fec3d278c09/bstein/test_12-13-16')

# Workflow
workflow = gbdx.Workflow([order_task, aop_task, crop_raster_task, openskynet_task, stage_task1, stage_task2, stage_task3])
workflow.execute()
print(workflow.id)
print(workflow.status)