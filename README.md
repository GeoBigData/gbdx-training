# intro
DigitalGlobe's Geospatial Big Data Platform, or GBDX, provides customers with a fast and easy way to search, order, and process DigitalGlobe imagery. We provide several tools for doing big data analytics on our platform, and the ability to leverage your own capabilities against your data or ours. This guide is provided to help discover the tools and resources you need to quickly and easily qet GBDX savvy.

# how to use these resources
What is it that you would like to get out of GBDX? We have resources for every type of user, categorized into different tracks below. Decide what kind of tools suit your needs and follow the steps within each track to find tutorials and documentation that will streamline your GBDX experience.

### AnswerFactory track:
This track is for users who would like to easily obtain information about imagery using pre-configured classification and feature extractions algorithms.
1. watch the recorded presentation ["GBDX Overview"](https://digitalglobe.wistia.com/medias/kbqln5pwks). The presentation slides are provided [here](https://docs.google.com/presentation/d/1SPsvbI6l1fO9zfeRTUSEdoV1M17bfYDp1xeCHWXfACU/edit?usp=sharing)
2. check out the [AnswerFactory module](./answerfactory_module/README.md) in this repo, which contains a guide to using AnswerFactory and a recorded demo
3. check out further documentation on AnswerFactory at [GBDX University](https://gbdxdocs.digitalglobe.com/docs/answerfactory-overview)

### GBDX APIs and Python track:
If you would like a python-friendly way of interacting with GBDX, learn how to use gbdxtools by taking the following steps:
1. watch the recorded presentation ["GBDX Overview"](https://digitalglobe.wistia.com/medias/kbqln5pwks). The presentation slides are provided [here](https://docs.google.com/presentation/d/1SPsvbI6l1fO9zfeRTUSEdoV1M17bfYDp1xeCHWXfACU/edit?usp=sharing)
2. check out the [gbdxtools module](./gbdxtools_module/README.md) in this repo, which includes videos and instructions on how to get set up with gbdxtools, example code, and a recorded demo
3. check out further documentation on gbdxtools at [gbdxtools readthedocs.io](http://gbdxtools.readthedocs.io/en/latest/)
4. optional: if you would like a convenient way to test the APIs, check out our Postman collections at [GBDX University](https://gbdxdocs.digitalglobe.com/docs/postman-instructions-collections)

### Custom Task track:
If you've developed a capability that you'd like to integrate with GBDX - to use with your tools and data and/or ours - learn how to dockerize your capability into a 'Task' that runs on GBDX by taking the following steps:
1. complete all of the steps that are listed in the gbdxtools track, being certain to install Docker and register for a Docker Hub account
2. check out the [Custom Task module](./custom_task_module/README.md) in this repo, which has instructions on how to dockerize your Task and a recorded demo
3. check out further documentation at [GBDX University](https://gbdxdocs.digitalglobe.com/docs/task-and-workflow-course)

### GBDX ninja track:
For a complete GBDX full immersion experience, you can work through each of the above tracks. Here are some milestones you can work towards while your learning.
- milestone #1: Download vector output from AnswerFactory and view in a GIS
- milestone #2: Order and pre-process imagery using gbdxtools, then locate the processed imagery in your customer S3 bucket
- milestone #3: Run an advanced Workflow, such as an LULC Workflow, on imagery and locate in your customer S3 bucket
- milestone #4: Register a Custom Task to GBDX using our 'clip_raster' example Task and locate your clipped image in your customer S3 bucket
- milestone #5: Register a Custom Task to GBDX using a capability/algorithm that you've developed and use it within a Workflow, locate the output of your Custom Task in your customer S3 bucket

___
### Resources

[__GBDX Web App__](https://gbdx.geobigdata.io/login)

[__AnswerFactory__](https://vector.geobigdata.io/answer-factory/login)

[__GBDX University__](https://gbdxdocs.digitalglobe.com/)

[__GBDXtools Documentation__](http://gbdxtools.readthedocs.io/en/latest/)

[__S3 Browser__](http://s3browser.geobigdata.io/login.html)

[__GBDX Stories__](http://gbdxstories.digitalglobe.com/)
___
We would love to hear your feedback. Feel free to email GBDX-support@digitalglobe.com with questions, comments or suggestions.
