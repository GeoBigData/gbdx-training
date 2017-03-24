#!/usr/bin/python

#############################################################################################
#
#  run_aop_acomp_clip.py
#
#  Created by: Dave Loomis
#              Digitalglobe GBD Solutions
#
#  Version 0.1: Jan 23, 2017
#               - run aop ortho, acomp and clip using gbdxtools
#
#  Usage: python run_aop_acomp_clip.py
#
#  This script will create a GBDX workflow that will create an ortho that has been acomped
#   and run raster clip on the result.  RasterClip will also move over the XML and IMD
#   files from the original AOP ortho
#
#  The script is dependent on gbdxtools 0.6.7 or greater to function correctly
#
#############################################################################################

from gbdxtools import Interface
gbdx = Interface()
gbdx_info = gbdx.s3.info

##### change your S3 destination directory
destination = 'my_directory/ntt_ortho'
##### add the catids to a list
catids = ['10400100250D3F00']

# this loop will create a new workflow for every catid
for catid in catids :
    # create the auto order task to place the catid order, or get the current location of the data
    #  This task will order the data if it doesn't exist in GBDX, or pass on the S3 data location
    #  to the next task in the workflow
    order_task = gbdx.Task("Auto_Ordering",cat_id=catid)
    order_task.impersonation_allowed = True
    data_loc = order_task.outputs.s3_location.value

    # # build the AOP task used in the workflow
    # This task will create an ortho with acomp from the input impage strip. Note that pansharp has been
    #  turned on and DRA is turned off
    # This task uses the GSI DEM
    aoptask = gbdx.Task("AOP_Strip_Processor", data=data_loc, enable_acomp=True, enable_pansharpen=True, enable_dra=False)
    # build the shp directory from the s3 information gathered above.
    #  gbdx.s3.info contains all of this
    #shp_dir = "s3://" + gbdx_info['bucket'] + "/" + gbdx_info['prefix'] + "/"
    # you will need to upload your shapefile here using "s3browser.geobigdata.io"
    #shp_dir = shp_dir + "dloomis/iraq_ecopia/shp"

    # declare the name of the output file with the "chip_name" field.  This could be anything
    #  but you could name the chip based on the shp or an number increment
    #  In this case I will name with a combination of catid + shp_name
    aop_clip = catid + "_" + "CLIP" + ".tif"
    # This task will clip the output AOP to the specified boundaries of the Shapefile
    #clip_task = gbdx.Task("RasterClip_Extents", raster=aoptask.outputs.data.value, chip_name=aop_clip,shp=shp_dir)

    ### OTHER RASTERCLIP OPTIONS ###
    # Use UL and LR coords to define chip area
    clip_task = gbdx.Task("RasterClip_Extents", raster=aoptask.outputs.data.value, chip_name=aop_clip,
                                                chip_ul_lr="135.39139,34.178110,135.568854,34.649")
    # Use POLYGON wkt
    #clip_task = gbdx.Task("RasterClip_Extents", raster=aoptask.outputs.data.value, chip_name=aop_clip,wkt="POLYGON ((-122.506172 37.693828,-122.388273 37.693828,-122.388273 37.772838,-122.506172 37.772838,-122.506172 37.693828))")

    # use this task to make tiles of the output
    #tile_task = gbdx.Task("gdal_tiler",data=clip_task.outputs.data.value,tiling_scheme='DGTiling',zoom_level='11',
    #                      tile_size='19584')

    # create the workflow
    workflow = gbdx.Workflow([order_task,aoptask,clip_task]) #,tile_task])
    # add the savedata commands to the workflow for each task that you want to save data out
    #  In this case, we are saving the clip task output
    workflow.savedata(aoptask.outputs.data, location=destination + "/" + catid + "/aop_data")
    workflow.savedata(clip_task.outputs.data, location=destination + "/" + catid)
    #workflow.savedata(tile_task.outputs.data, location=destination + "/" + catid)

    # kick off the workflow.  "generate_workflow_description"
    #print(workflow.generate_workflow_description())
    #print
    #raise
    workflow.execute()

    # print out the workflow.status, this is one way to get the workflow id and the status
    print
    print(workflow.id)
    print(workflow.status)
