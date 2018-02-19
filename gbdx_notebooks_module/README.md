## intro
GBDX Notebooks is hosted Python environment that provides immediate access to analysis-ready imagery in a familiar Jupyter Notebook environment. This environment is preconfigured with data science and geoprocessing tools that make it easy to develop new analysis methods and run them at scale on GBDX.

## what you will learn
The notebook tutorials listed below are designed to guide you through the basics of coding against imagery in the notebook to deploying an algorithm and running it at scale on GBDX.

## to get started
- sign into the [GBDX Notebooks Hub](https://notebooks.geobigdata.io) using your GBDX credentials
- select a tutorial from below (they progress from very basic to advanced)
- click the notebook link, which will take you to the tutorial notebook in the GBDX Notebook Hub
- click "Clone and Edit" to create your own personal version of the notebook
- follow the instructions in the notebook to complete the tutorial

## tutorials

__1. GBDX Notebook basics__ - [notebook link](https://notebooks.geobigdata.io/hub/notebooks/5a57f08fb72f7f5bf2ef326e)

Learn to navigate the notebook interface, how to write and execute code in the notebook, plot a graph, and start a blank notebook.

new methods: basic python exercises

__2. Simple NDVI__ - [notebook link](https://notebooks.geobigdata.io/hub/notebooks/5a57f08fb72f7f5bf2ef326e)

Learn how to fetch image pixel data and view it in the notebook, then run an easy vegetation analysis on the imagery.

new methods: plot imagery, array operations

__3. Algorithm prototyping__ - [notebook link](https://notebooks.geobigdata.io/hub/notebooks/5a57f08fb72f7f5bf2ef326e)

In this Notebook, we walk through a simple methodology for extracting coastlines from 8-band multispectral imagery. This tutorial demonstrates how to link together several concepts from remote sensing, image science, and GIS to produce a complete geospatial analysis. The steps in the workflow include: (1) calculating a Normalized Difference Water Index; (2) thresholding the water index into a binary image; (3) cleaning up small features; and (4) converting the land/water boundaries into vector polylines representing coastlines.

new methods: image metadata, more array operations

__4. Algorithm scaling__ - [notebook link](https://notebooks.geobigdata.io/hub/notebooks/5a58317a8aeae044c479bf20)

In this Notebook, we will extend the simple methodology for extracting coastlines that we built in the previous tutorial. Our goal in this Notebook is to be able to run the same methodology over a much bigger geographic area. Specifically, we are going to show two different approaches to running the algorithm over an entire image rather than just one small part of that image, like we used last time.

new methods: pip install, edge cases, downsampling, generate image chips, edge effects, strips vs chips, image affine, easy method for viewing results on a map

__5. Deploy algorithm as a Task__ - [notebook link](https://notebooks.geobigdata.io/hub/notebooks/5a6657eaaa91896cfe650558)

In this Notebook, we provide a walkthrough of how to deploy our coastline extraction algorithm as a GBDX Task, using some helpful tools built right into the GBDX Notebooks interface. Once we've done this, we can execute the same Task against multiple images all at the same time: each will be kicked off as a separate, parallel workflow, without being constrained to the computational limits of a single machine.

new methods: how to set Task inputs and outputs, save output to geojson, Task deploy, run Task in notebook

__6. Run algorithm as a Task on GBDX__ - [notebook link](https://notebooks.geobigdata.io/hub/notebooks/5a691c0caa91896cfe65060c)

In the previous Notebook, we walked through how to deploy our coastline extraction algorithm as a GBDX Task, enabling us to run it on the GBDX platform instead of inside of our Notebook. In this final Notebook, we are going to use the GBDX Task we created to run coastline extraction over multiple images, in parallel, using GBDX Workflows. Using this approach, we'll be able to extract a highly detailed coastline for the entire island of Kauai, in less than 10 minutes.

new methods: running a Task in a Workflow, tracking Task and Workflow status, locating output in S3, vizualizing Workflow output in the notebook

## take it further

There are several notebooks in the GBDX Notebooks Hub that demonstrate useful methods and tools, you will find them in the Discover section. Here is a short list of recommended notebooks.

[Searching and Ordering Imagery](www.google.com)

[Workflow Basics](www.google.com)

[Ordering and Working with Imagery](https://notebooks.geobigdata.io/hub/notebooks/5a0370dfe21cea77cee2436b)
<br />
new methods: search and order imagery to GBDX

[Imagery and Areas of Interest](https://notebooks.geobigdata.io/hub/notebooks/5a037c12f74cf64a53479964)
<br />
new methods:index an image with different types of geometries, the image geointerface

[Base Layer Matching to Maps API](https://notebooks.geobigdata.io/hub/notebooks/5a70d42b2966da03cacf765e)
<br />
new methods: generate color balanced imagery with histogram matching

[Color Matching Imagery to Browse Imagery](https://notebooks.geobigdata.io/hub/notebooks/5a29c32256e0d252e24aa1f5)
<br />
new methods: color balancing for very light or dark imagery
