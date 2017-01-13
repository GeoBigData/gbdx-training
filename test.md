# (TO DOs)
- purpose of tutorial, assumtions about user knowledge before starting this tutorial, link to pre-reqs, etc
- [X]use os library to write i/o
- [X]create output directory to write out masked tif
- add explanation of what script is doing
- add short explanations/intro for each segment
- keep commented out lines?
- fix Dockerfile (left off in middle of editing)
- write i/o cheatsheet
- show how test script within Docker container 
- add test files (test the test files)
- add TOC hyperlinks 
- troubleshooting? (Dockerfile extension)


## step 1) write and test algorithm that processes locally 
here is an example python script that clips a raster image using a shapefile (need to explain how)
  ```python
  import fiona
  import rasterio
  import os
  import glob

  in_path = os.path.join(os.path.expanduser('~'), 'documents', 'demo', 'input')
  ward_shape = glob.glob(in_path + '/*.shp')
  ward_image = glob.glob(in_path + '/*.tif')
  
  out_path = os.path.join(os.path.expanduser('~'), 'documents', 'demo', 'output')
  os.chdir(out_path)
  
  with fiona.open(shapefile, "r") as shapefile:
      features = [feature["geometry"] for feature in shapefile]

  with rasterio.open(image) as src:
      out_image, out_transform = rasterio.tools.mask.mask(src, features, crop=True)
      out_meta = src.meta.copy()
  
  out_meta.update({"driver": "GTiff",
                   "height": out_image.shape[1],
                   "width": out_image.shape[2],
                   "transform": out_transform})

  with rasterio.open("masked.tif", "w", **out_meta) as dest:
      dest.write(out_image)
  ```

## step 2) modify to match I/O structure within Docker container
(short explanation about platform orchestrating data movement within docker container and i/o naming conventions)
  ```python
  import fiona
  import rasterio
  import os
  import glob

  # in_path = os.path.join(os.path.expanduser('~'), 'documents', 'demo', 'input')
  in_path = '/mnt/work/input/data_in'
  ward_shape = glob.glob(in_path + '/*.shp')
  ward_image = glob.glob(in_path + '/*.tif')
  
  # out_path = os.path.join(os.path.expanduser('~'), 'documents', 'demo', 'output')
  out_path = '/mnt/work/output/data_out'
  os.chdir(out_path)
  
  with fiona.open(shapefile, "r") as shapefile:
      features = [feature["geometry"] for feature in shapefile]

  with rasterio.open(image) as src:
      out_image, out_transform = rasterio.tools.mask.mask(src, features, crop=True)
      out_meta = src.meta.copy()
  
  out_meta.update({"driver": "GTiff",
                   "height": out_image.shape[1],
                   "width": out_image.shape[2],
                   "transform": out_transform})

  with rasterio.open("masked.tif", "w", **out_meta) as dest:
      dest.write(out_image)
  ```

## write Dockerfile 
(explantion about why, what it does, best practices, etc)
  ```
  FROM ubuntu:14.04
  RUN apt-get update && apt-get -y install\
    python \
    vim\
    build-essential\
    python-software-properties\
    software-properties-common\
    python-pip\
    python-dev
  RUN mkdir /
  ADD ./bin /training-indices
  CMD python /training-indices/mud_water_indices.py
  ```
