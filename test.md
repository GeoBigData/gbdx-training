## local script

Step 1) Write an algorithm that successfully processes imagery in the way you intend on your local machine

Here is an example script that clips a raster image using a shapefile
  ```
  import fiona
  import rasterio
  from rasterio.tools.mask import mask

  shapefile = '/Users/elizabethgolden/Downloads/shpefiel'
  image = '/Users/elizabethgolden/Downloads/055636722010_01_assembly_MS_clip.tif'

  with fiona.open(shapefile, "r") as shapefile:
      features = [feature["geometry"] for feature in shapefile]

  with rasterio.open(image) as src:
      out_image, out_transform = mask(src, features, crop=True)
      out_meta = src.meta.copy()
  ```
