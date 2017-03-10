import fiona
import rasterio
import rasterio.mask
import os
import glob

# set the input ports path
# note, we define this when we register the task so GBDX will create this directory
# and load the data into it when the docker loads
in_path = '/mnt/work/input'
shape_path = in_path + '/input_shapefile'
image_path = in_path + '/input_image'

# search tne input shapefile port for the first shapefile that we specify in the call to this task
my_shape = glob.glob1(shape_path, '*.shp')[0]

# search the input image port for the first geotiff that we specify in the call to this task
my_image = glob.glob1(image_path, '*.tif')[0]

# define the name of the output data port
# note, we define this when we register the task so GBDX will create this directory
out_path = '/mnt/work/output/data_out'

# while the input ports are created by GBDX, we will need to create the output data port
if os.path.exists(out_path) == False:
  os.makedirs(out_path)

# change directories to the output data port
os.chdir(out_path)

# open the input shapefile and get the polygon features for clipping
with fiona.open(os.path.join(shape_path, my_shape), "r") as shapefile:
  features = [feature["geometry"] for feature in shapefile]

# open the input image, clip the image with the shapefile and get the image metadata
with rasterio.open(os.path.join(image_path, my_image)) as src:
  out_image, out_transform = rasterio.mask.mask(src, features, crop=True)
  out_meta = src.meta.copy()

# write out the metadata to the image
out_meta.update({"driver": "GTiff",
  "height": out_image.shape[1],
  "width": out_image.shape[2],
  "transform": out_transform})

# write out the output image
with rasterio.open("masked.tif", "w", **out_meta) as dest:
  dest.write(out_image)

# OPTIONAL: OUTPUT STATUS FILE TO GIVE THE USER MORE FEEDBACK
# a status file always needs to be present to populate with the operation status
# status = {}
# status['status'] = 'Success'
# status['reason'] = "===== Task successfully completed ======"

# write the json status
# with open('/mnt/work/status.json', 'w') as statusfile:
#         json.dump(status,statusfile)
