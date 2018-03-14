# Quickstart
Want to see what GBDX can do? Follow the links below to view examples of combining the power of immediate imagery access with additional data sources to derive information and insight. Although it took a lot of coding to create the analyses, you can simply scroll through the webpage to view not only the code, but also view results in an interactive map. 

### [Imagery to Insights with GBDX - Boat Traffic](https://notebooks.geobigdata.io/hub/notebooks/5a931838bf151131f290fe26?tab=code)

This Notebook demonstrates how to quickly go from imagery to insight by combining a boat extraction analysis with weather data to gain meaningful insights about boat traffic near Point Piper, Australia.
<img src="https://s3.amazonaws.com/gbdx-training/esg_images/boats.png" style="float: right; width: 600px; margin-right: 40px; margin-left: 40px; margin-bottom: 40px">

### [Ecopia Building Footprints and GBDX](https://notebooks.geobigdata.io/hub/notebooks/5a87205bbf151131f290fd51?tab=code)

DigitalGlobe has partnered with Ecopia to produce highly accurate, up-to-date 2D building footprints. In this Notebook, we
demonstrate how to analyze those building footprints against the original source imagery to create an enhanced dataset. Combining these datasets with the power of GBDX gives us quick and powerful insight into new business use cases and research questions.

<img src="https://s3.amazonaws.com/gbdx-training/esg_images/footprints.png" style="float: right; width: 600px; margin-right: 40px; margin-left: 40px; margin-bottom: 40px">

# Intro
DigitalGlobe's Geospatial Big Data Platform, or GBDX, provides customers with a fast and easy way to search, order, and process DigitalGlobe imagery. We provide several tools for doing big data analytics on our platform, and the ability to leverage your own capabilities against your data or ours. This guide is provided to help discover the tools and resources you need to quickly and easily start developing on GBDX.

# GBDX Overview
In this presentation, we explain what GBDX is, why we built it, we'll highlight solutions that partners are building on GBDX, and introduce important technical concepts. These technical concepts will be covered in more detail in the hands-on tutorials.

[GBDX Overview recorded presentation](https://digitalglobe.wistia.com/medias/kbqln5pwks)

[GBDX Overview slides](https://docs.google.com/presentation/d/1SPsvbI6l1fO9zfeRTUSEdoV1M17bfYDp1xeCHWXfACU/edit?usp=sharing)

# GBDX and Python: GBDX Notebooks
The quickest, easiest way to get started on GBDX. Start coding Python against DigitalGlobe imagery in a hosted Jupyter Notebook environment. You don't need to install anything and there are easy tools for searching and loading imagery directly in the notebook.

These tutorials cover the skills and concepts you need to start developing on GBDX with Python. The tutorials progress from learning the basics of coding in the Notebook, to developing robust analysis methods and deploying them at scale on GBDX, and will also cover foundational skills such as searching the Catalog and ordering imagery to GBDX.

You'll find all the resources to get started on GBDX in the [GBDX Notebooks module](../gbdx_notebooks_module) in this repo.

# GBDX and Python: Direct Access

The tutorials and resources in this section are provided to help you transition from developing via GBDX Notebooks to developing in your local Python environment. This requires installing additional libraries and software, but also provides greater flexibility and integration with your existing analysis tools.

### Install gbdxtools 

gbdxtools is a Python library for interacting with the GBDX API. If you've worked on any of the GBDX Notebooks tutorials, then you've used gbdxtools. 

The instructions in this module will help you install gbdxtools in your local development environment, where it's easy to integrate your GBDX workflow with your existing analysis tools. Once you've installed gbdxtools, you can code against DigitalGlobe imagery in exactly the same way as you did in the GBDX Notebooks tutorials, using the same gbdxtools code and commands. 

Find these instructions in the [gbdxtools module](../gbdxtools_module) in this repo.

### Custom Task tutorial
Once you're ready to turn your analysis methods into production-ready analysis tools, you can package your code and dependencies into a Docker, then register it as a Task on GBDX. From there, it's simple to run that Task as many times as you want on as much imagery as you need.

If you completed the tutorials from the GBDX Notebooks module, you've already registered a Task on GBDX and used it in a Workflow. In that environment, GBDX Notebooks automatically handled all of the Task registration steps for you. 

In this tutorial, we demonstrate how to manually register a Task to GBDX. We provide the code for an example Task, and walk you through the steps of Dockerizing that code, registering it as a Task, then running it in a Workflow on GBDX. This will allow you the greatest flexibility in creating your own, custom analysis tools and running them at scale. 

Find these instructions in the [Custom Task module](../custom_task_module) in this repo.

___
### Resources

[__GBDX University__](https://gbdxdocs.digitalglobe.com/)

[__GBDX Notebooks Hub__](https://notebooks.geobigdata.io)

[__GBDXtools Documentation__](http://gbdxtools.readthedocs.io/en/latest/)

[__S3 Browser__](http://s3browser.geobigdata.io/login.html)

[__GBDX Stories__](http://gbdxstories.digitalglobe.com/)
___
We would love to hear your feedback. Feel free to email GBDX-support@digitalglobe.com with questions, comments or suggestions.
