## intro
GBDX Notebooks is a hosted Python environment that provides immediate access to analysis-ready imagery in a familiar Jupyter Notebook environment. This environment is preconfigured with data science and geoprocessing tools that make it easy to develop new analysis methods and run them at scale on GBDX.

## what you will learn
The notebook tutorials listed below are designed to guide you through the basics of coding against imagery in the notebook to deploying an algorithm and running it at scale on GBDX.

## to get started
- sign into the [GBDX Notebooks Hub](https://notebooks.geobigdata.io) using your GBDX credentials
- link to your Github account [(instructions here)](https://gbdxdocs.digitalglobe.com/docs/gbdx-notebooks-course#section-getting-started)
- select a tutorial from below (they progress from very basic to advanced)
- follow the link to the tutorial notebook in the GBDX Notebook Hub
- click "Clone and Edit" to create your own private version of the notebook
- follow the instructions in the notebook to complete the tutorial

## tutorials

__1. [GBDX Notebook basics](https://notebooks.geobigdata.io/hub/notebooks/5b27f7db2c7831647a306e3c?tab=code)__  `python exercises`

Learn to navigate the notebook interface, how to write and execute code in the notebook, plot a graph, and start a blank notebook.

__2. [Simple NDVI](https://notebooks.geobigdata.io/hub/notebooks/5b27f8262c7831647a306e3f?tab=code)__  `view image`  `array operations`  `NDVI`

Learn how to fetch image pixel data and view it in the notebook, then run an easy vegetation analysis on the imagery.

__3. [Algorithm prototyping](https://notebooks.geobigdata.io/hub/notebooks/5b27f9862c7831647a306e49?tab=code)__  `NDWI`  `coastline extraction` 

In this Notebook, we walk through a simple methodology for extracting coastlines from 8-band multispectral imagery. This tutorial demonstrates how to link together several concepts from remote sensing, image science, and GIS to produce a complete geospatial analysis. The steps in the workflow include: (1) calculating a Normalized Difference Water Index; (2) thresholding the water index into a binary image; (3) cleaning up small features; and (4) converting the land/water boundaries into vector polylines representing coastlines.

__4. [Algorithm scaling](https://notebooks.geobigdata.io/hub/notebooks/5b27f82b2c7831647a306e41?tab=code)__  `pip install`  `edge cases`  `image chips`  `image affine`  `visualization`

In this Notebook, we will extend the simple methodology for extracting coastlines that we built in the previous tutorial. Our goal in this Notebook is to be able to run the same methodology over a much bigger geographic area. Specifically, we are going to show two different approaches to running the algorithm over an entire image rather than just one small part of that image, like we used last time.

__5. [Deploy algorithm as a Task](https://notebooks.geobigdata.io/hub/notebooks/5b27f8532c7831647a306e42?tab=code)__  `task inputs`  `task outputs`  `task deploy`  

In this Notebook, we provide a walkthrough of how to deploy our coastline extraction algorithm as a GBDX Task, using some helpful tools built right into the GBDX Notebooks interface. Once we've done this, we can execute the same Task against multiple images all at the same time: each will be kicked off as a separate, parallel workflow, without being constrained to the computational limits of a single machine.

__6. [Run algorithm as a Task on GBDX](https://notebooks.geobigdata.io/hub/notebooks/5b27f8282c7831647a306e40?tab=code)__  `workflows`  `S3 output`  `vizualizing output`

In the previous Notebook, we walked through how to deploy our coastline extraction algorithm as a GBDX Task, enabling us to run it on the GBDX platform instead of inside of our Notebook. In this final Notebook, we are going to use the GBDX Task we created to run coastline extraction over multiple images, in parallel, using GBDX Workflows. Using this approach, we'll be able to extract a highly detailed coastline for the entire island of Kauai, in less than 10 minutes.

## next steps

There are several notebooks in the GBDX Notebooks Hub that demonstrate useful methods and tools, you will find them in the Discover section. Here is a short list of recommended notebooks.
 
[Searching and Ordering Imagery](https://notebooks.geobigdata.io/hub/notebooks/5b27f7db2c7831647a306e3d?tab=code)  `catalog search`  `order imagery`

[Workflow Basics](https://notebooks.geobigdata.io/hub/notebooks/5b27f7da2c7831647a306e3b?tab=code)  `tasks`  `workflows`  `image preprocessing`  `task inputs and outputs`  `s3 output`

[Imagery and Areas of Interest](https://notebooks.geobigdata.io/hub/notebooks/5a037c12f74cf64a53479964?tab=code)  `index image with various geometries`  `image geointerface` 

[Color Matching Imagery to Browse Imagery](https://notebooks.geobigdata.io/hub/notebooks/5a29c32256e0d252e24aa1f5?tab=code)  `color balancing for light or dark imagery`


___
### Resources

[__GBDX University__](https://gbdxdocs.digitalglobe.com/)

[__GBDX Notebooks Hub__](https://notebooks.geobigdata.io)

[__GBDXtools Documentation__](http://gbdxtools.readthedocs.io/en/latest/)

[__S3 Browser__](http://s3browser.geobigdata.io/login.html)

[__GBDX Stories__](http://gbdxstories.digitalglobe.com/)
___
We would love to hear your feedback. Feel free to email GBDX-support@digitalglobe.com with questions, comments or suggestions.

