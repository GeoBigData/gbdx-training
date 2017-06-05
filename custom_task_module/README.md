# intro
Users can and are encouraged to build their own custom analytic capability, what we call a 'Task', to use within the Workflow system on GBDX.  

# what you will learn
This tutorial will walk you through the multi-step process of putting a Task on GBDX, starting with some sample code that clips a raster to a shapefile as our example Task. The provided tutorial notebook walks you through each step, and if you execute the blocks of code as you follow along, will write out the files that are necessary to the Task registration process directly to your computer. Feel free to follow the steps and write your own files outside of the notebook if you prefer.  

# to get started
It is strongly recommended that you follow the steps for the gbdxtools track first, as that will give you the background knowledge to understand how your Task will integrate with GBDX, and because you will need gbdxtools in order to register your Task and test it within a Workflow. 

__Install gbdxtools and Docker__
1. Instructions for installing gbdxtools can be found in the gbdxtools module of this repo
2. Install Docker from https://www.docker.com/
3. Test your Docker installation by starting Docker and pasting in the following command, which should return your Docker version 
```
docker version
```
4. Sign up for a free Docker Hub account at https://hub.docker.com/

__Download and start the Notebook tutorial:__
1. Download the file custom-task-tutorial.ipynb from this repository.

2. Open a terminal/cmd window and copy and paste `jupyter notebook`. This will open the Jupyter Notebook interface in your browser [(documentation here)](https://jupyter.readthedocs.io/en/latest/running.html#running). 

3. Within in the Jupyter Notebook interface, navigate to where you saved the custom-task-tutorial.ipynb file and click on it to start the notebook.

4. The custom-task-tutorial.ipynb explains all of the steps required to register a custom task to GBDX, along with example code. You can execute the code within the notebook by using the keyboard shortcut SHIFT + ENTER, or select the play button in the toolbar. Follow the instructions in the notebook and optionally watch the [recording of this tutorial](https://digitalglobe.wistia.com/medias/8z9hj4g960). 

___
We would love to hear your feedback. Feel free to email GBDX-support@digitalglobe.com with comments and suggestions.
