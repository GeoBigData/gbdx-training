# Intro
DigitalGlobe's Geospatial Big Data Platform, or GBDX, provides customers with a fast and easy way to search, order, and process DigitalGlobe imagery. We provide several tools for doing big data analytics on our platform, and the ability to leverage your own capabilities against your data or ours. This guide is provided to help discover the tools and resources you need to quickly and easily start developing on GBDX.

## GBDX Overview
In this presentation, we explain what GBDX is, why we built it, we'll highlight solutions that partners are building on GBDX, and introduce important technical concepts. These technical concepts will be covered in more detail in the hands-on tutorials.

[GBDX Overview recorded presentation](https://digitalglobe.wistia.com/medias/kbqln5pwks)

[GBDX Overview slides](https://docs.google.com/presentation/d/1SPsvbI6l1fO9zfeRTUSEdoV1M17bfYDp1xeCHWXfACU/edit?usp=sharing)

## GBDX and Python: GBDX Notebooks
The quickest, easiest way to get started on GBDX. Start coding Python against DigitalGlobe imagery in a hosted Jupyter Notebook environment. You don't need to install anything and there are easy tools for searching and loading imagery directly in the notebook.

These tutorials cover the skills and concepts you need to start developing on GBDX with Python. The tutorials progress from learning the basics of coding in the Notebook, to developing robust analysis methods and deploying them at scale on GBDX, and will also cover foundational skills such as searching the Catalog and ordering imagery to GBDX.

You'll find all the resources to get started on GBDX in the [GBDX Notebooks module](../gbdx_notebooks_module) in this repo.

## GBDX and Python: Direct Access

The tutorials and resources in this section are provided to help you transition from developing via GBDX Notebooks to developing in your local Python environment. This requires installing additional libraries and software, but also provides greater flexibility and integration with your existing analysis tools.

### Install gbdxtools 

gbdxtools is a Python library for interacting with the GBDX API. If you've completed any of the GBDX Notebooks tutorials, then you've used gbdxtools. 

The instructions in this module will help you install gbdxtools in your local development environment, where it's easy to integrate your GBDX workflow with your existing analysis tools. Once you installed gbdxtools, you can code against DigitalGlobe imagery in exactly the same way as you did in the GBDX Notebooks tutorials, using the same gbdxtools commands. 

Find these instructions in the [gbdxtools module](../gbdxtools_module) in this repo.

### Custom Task tutorial
Once you're ready to turn your analysis methods into production-ready analysis tools, you can package your code and dependencies into a Docker, then register it as Task on GBDX. From there, it's simple to run that Task as many times as you want on as much imagery as you need.

If you completed the tutorials from the GBDX Notebooks module, you already registered a Task on GBDX and ran it in a Workflow. You didn't have to Dockerize your code or register it on GBDX, however, because GBDX Notebooks handles these steps for you.

We provide a tutorial that will walk you through these steps in your local development environment in the [Custom Task module](../custom_task_module) in this repo. 

___
### Resources

[__GBDX University__](https://gbdxdocs.digitalglobe.com/)

[__GBDX Notebooks Hub__](https://notebooks.geobigdata.io)

[__GBDXtools Documentation__](http://gbdxtools.readthedocs.io/en/latest/)

[__S3 Browser__](http://s3browser.geobigdata.io/login.html)

[__GBDX Stories__](http://gbdxstories.digitalglobe.com/)
___
We would love to hear your feedback. Feel free to email GBDX-support@digitalglobe.com with questions, comments or suggestions.
