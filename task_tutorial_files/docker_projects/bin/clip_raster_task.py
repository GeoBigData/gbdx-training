
import fiona
import rasterio
import rasterio.mask
import os
import glob

# set the input ports path
in_path = '/mnt/work/input'
shape_path = in_path + '/input_shapefile'
raster_path = in_path + '/input_raster'

# search the input shapefile port for the first shapefile that we specify in the call to this task
my_shape = glob.glob1(shape_path, '*.shp')[0]

# search the input image port for the first geotiff that we specify in the call to this task
my_raster = glob.glob1(raster_path, '*.tif')[0]

# define the name of the output data port
out_path = '/mnt/work/output/data_out'

# create the output data port
if os.path.exists(out_path) == False:
  os.makedirs(out_path)

# change directories to the output data port
os.chdir(out_path)

# open the input shapefile and get the polygon features for clipping
with fiona.open(os.path.join(shape_path, my_shape), "r") as shapefile:
  features = [feature["geometry"] for feature in shapefile]

# open the input image, clip the image with the shapefile and get the image metadata
with rasterio.open(os.path.join(raster_path, my_raster)) as src:
  out_raster, out_transform = rasterio.mask.mask(src, features, crop=True)
  out_meta = src.meta.copy()

# write out the metadata to the raster
out_meta.update({"driver": "GTiff",
  "height": out_raster.shape[1],
  "width": out_raster.shape[2],
  "transform": out_transform})

# write out the output raster
with rasterio.open("masked.tif", "w", **out_meta) as dest:
  dest.write(out_raster)
