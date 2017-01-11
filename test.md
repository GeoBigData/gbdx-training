## Step 1) write algorithm that processes locally 
Here is an example script that clips a raster image using a shapefile
  ```
  import fiona
  import rasterio
  from rasterio.tools.mask import mask

  shapefile = <path to shapefile>
  image = <path to image>
  
  with fiona.open(shapefile, "r") as shapefile:
      features = [feature["geometry"] for feature in shapefile]

  with rasterio.open(image) as src:
      out_image, out_transform = mask(src, features, crop=True)
      out_meta = src.meta.copy()
  ```
