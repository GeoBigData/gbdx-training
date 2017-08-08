## intro
Please follow the steps below to ensure that your system is setup and tested prior to an in-person GBDX training or workshop.

By the end of this walkthrough, you should have:
- GBDX credentials including your client ID and client secret
- installed: Anaconda, gbdxtools, Docker
- successfully run the provided test Jupyter Notebook with your GBDX credentials
- signed up for a free Docker Hub account
- pulled and pushed an example Docker image to Docker Hub

## to get started
GBDXtools is a GBDX Python package that allows one to easily access GBDX APIs to search the DigitalGlobe catalog, and order and process imagery.

The following steps walk you through an easy, proven way of installing gbdxtools and its dependencies on Mac, Windows or Linux.

__1. Install Anaconda__
The first required step is to install Anaconda, an open source Python distribution that simplifies package management, dependencies, and environments (we recommend this step even if you already have a Python installation). This distribution includes Conda, which you will need in order to install gbdxtools using the provided conda environment file, and Jupyter Notebook, which you'll need to run the provided Jupyter Notebook that contains the gbdxtools tutorial.

__1.1__ Download and install the **full version** of [Anaconda](https://www.continuum.io/downloads)

Requirements:
- All users:
	- Python 2.7 version
		- *this should not not interfere with other Python versions you may already have*
    - 64-Bit is preferred
    - Make sure to install the full version Anaconda and not Miniconda to ensure all required dependencies are included
- Windows users:
	- During the installation, please check the box that sets Path values when prompted
		- *please do this even though it is not the default setting*

__2. Install gbdxtools__

We have provided a Conda environment file for easy installion of gbdxtools, along with its required dependencies, within a Conda virtual environment. Virtual environments keep the dependencies required by different projects in separate places, so that they don't interfere with each other. Please use the following Conda commands to install gbdxtools.

Mac users:

__2.1__ Download the [gbdxtools_env.yml](../gbdxtools_module/gbdxtools_env.yml) file from this repo

__2.2__ Open a terminal window

__2.3__ Update conda
```
conda update conda
```
__2.4__ Create the conda environment
```
conda env create -f /full/path/to/gbdxtools_env.yml
```
__2.5__ Activate the environment
```
source activate gbdxtools
```
__2.6__ Try importing all the modules (if no errors are raised, everything is working right)
```
python -c 'import rasterio; import fiona; import shapely; import gbdxtools'
```

Windows users:

__2.1__ Download the [gbdxtools_env.yml](../gbdxtools_module/gbdxtools_env.yml) file from this repo

__2.2__ Open cmd.exe

__2.3__ Update conda
```
conda update conda
```
__2.4__ Create the conda environment
```
conda env create -f C:\\full\path\to\gbdx_environment.yml
```
__2.5__ Activate the environment
```
activate gbdxtools
```
__2.6__ Try importing all the modules (if no errors are raised, everything is working right)
```
python -c "import rasterio; import fiona; import shapely; import gbdxtools"
```

__3. Activate your GBDX acount credentials and locate your API key__

__3.1__ Activate your account - once you've been assigned to your company's GBDX account (we will do this for you, please coordinate with your company's GBDX POC), you should receive an email from DigitalGlobe instructing you to activate your account. Open the message and click on "ACTIVATE YOUR ACCOUNT". This will pop up a window in your browser where you will prompted to set a password.

__3.2__ Sign in to the [GBDX Web App](https://gbdx.geobigdata.io) with your GBDX username and password.

__3.3__ Find your profile - first click the user icon in the lower left corner, then your username.

__3.4__ Look for the strings called “Client ID” and “Client Secret.” These are the GBDX credentials you'll need later to authenticate into GBDX using gbdxtools. 

__4. Start Jupyter Notebook and authenticate into GBDX__

Jupyter Notebook is an open-source web application that makes it easy to create and share documents - called Notebooks - that contain live code and explanatory text. When you start the app, it will launch a Python 'kernel' and the Notebook Dashboard from your browser. From here, you can open and close Notebooks and manage running kernels [(documentation here)](https://jupyter.readthedocs.io/en/latest/running.html#running). Use the following instructions to start the provided gbdxtools test Notebook.

__4.1__ Download the file `gbdxtools-test.ipynb` from this repository.

__4.2__ Open a terminal/cmd window and navigate to the directory where you saved gbdxtools-test.ipynb.

__4.3__ Start the Jupyter Notebook app.
```
jupyter notebook
```
__4.4__ Click gbdxtools-test.ipynb to launch the Notebook.

__4.5__ Switch to the gbdxtools environment kernel:
- select the "Kernel" dropdown menu from the toolbar
- hover over "Change Kernel"
- select Python [conda env:gbdxtools]

__4.5__ Follow the directions that demonstrate how to run code in a Notebook and test the GBDX credentials you retrieved in step 3.

__Docker__

Docker is a software containerization techonology that makes it easy to share software in lightweight, portable packages. We use Docker technology to package up custom algorithms and run them against imagery in the cloud.

__5. Sign up for a Docker Hub account__

__5.1__ Sign up for a free Docker Hub account at https://hub.docker.com/

__6. Install Docker and test__

__6.1__ Install Docker from https://www.docker.com/ (some Windows users may need to install Docker Engine)

__6.2__ Start the Docker app.

__6.3__ Bring up a terminal/cmd window. The following Docker command will return your Docker version.
```
docker --version
```

__6.4__ Test pull a Docker image: Use the following command to pull the miniconda image from Docker Hub. Miniconda is a lighweight alternative to Anaconda that is simply the Conda package manager and its dependencies.
```
docker pull continuumio/miniconda
```
__6.6__ Confirm that the image downloaded, you should see it listed it when you use the following command.
```
docker images
```
__6.7__ Tag the image so that you can edit it and push it to your own repository. Replace <username> with your Docker Hub username.
```
docker tag continuumio/miniconda <username>/miniconda-docker
```

__6.8__ Test push a Docker image: first, log in to Docker Hub using your Docker Hub username and password.
```
docker login -u <username> -p <password>
```

__6.9__ Test push a Docker image: Use the following command to push your tagged image to your Docker Hub account. Remember to replace <username> with your Docker Hub username. This may take a few minutes, but it should appear as a repository on Docker Hub under your account.
```
docker push <username>/miniconda-docker
```

__7. Shut it all down__

When you are finished with this tutorial, shut down the Jupyter Notebook and kernel, and deactivate the Conda environment where you installed gbdxtools.

__7.1__ Stop the Jupyter Notebook by typing `CONTROL + C`, then `'Y'` to confirm that you would like to shut down the notebook server.

Mac users:
__7.2__ Deactivate the virtual environment
```
source deactivate
```
__7.3__ (Optional) Remove the environment
```
conda remove --name gbdxtools --all
```

Windows users:
__7.2__ Deactivate the virtual environment
```
deactivate gbdxtools
```
__7.3__ (Optional) Remove the environment

```
conda remove --name gbdxtools --all
```
___

__8. Optional .gbdx-config file:__

Save a gbdxtools config file to your home directory with your GBDX credentials. This will allow you to authenticate a gbdxtools session without needing to enter your credentials each time.

__8.1__ You will need your GBDX credentials again (located within your profile information in the [GBDX Web App](https://gbdx.geobigdata.io/profile)).

__8.2__ Create a blank text file and copy and paste the following information:
    ```
    [gbdx]
    auth_url = https://geobigdata.io/auth/v1/oauth/token/
    client_id = <your_client_id>
    client_secret = <your_client_secret>
    user_name = <your_user_name>
    user_password = <your_password>
    ```
__8.3__ Replace `<your_client_id>` and `<your_client_secret>` with your credentials, also `<your_user_name>` and `<your_password>` with the username and password associated with your GBDX account.

__8.4__ Save this file in your home directory with the filename `.gbdx-config`
	- be sure to include the `.` at the beginning of the filename
	- the filename needs to be saved without an extension

__8.5__ Test your gbdxtools installation and config file:
	- Open a terminal/cmd window and type `python`
	- Copy and paste the following code, which will result in an error if it can't locate your config file or if the formatting is incorrect

   ```python
   from gbdxtools import Interface
   gbdx = Interface()
   ```
   - Once you are done, quit Python by typing `exit()`


Config file troubleshooting:

Windows: select the filename and try to delete the '.txt' extension. You may need to save it as `.gbdx-config.` (notice the trailing period). Also, deselect the 'hide extensions' setting on your computer so you can verify if you've successfully deleted the extension.

Mac: select the config file, right-click and select 'Get Info' to verify that you've saved the file without an extension.

___

We would love to hear your feedback. Feel free to email GBDX-support@digitalglobe.com with comments and suggestions.
