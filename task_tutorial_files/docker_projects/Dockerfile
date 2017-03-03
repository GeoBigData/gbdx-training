FROM continuumio/miniconda

RUN conda install rasterio
RUN conda install fiona

RUN mkdir /my_scripts
ADD ./bin /my_scripts
CMD python /my_scripts/clip_raster_task.py