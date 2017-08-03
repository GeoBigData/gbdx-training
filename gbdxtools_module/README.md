## intro
GBDXtools is a GBDX Python package that allows one to easily access GBDX APIs to search the DigitalGlobe catalog, and order and process imagery.

## what you will learn
In this tutorial, we'll demonstrate how to search the DigitalGlobe archive via the Catalog API, order imagery using the Order API, and run an analysis workflow with the Workflow API.

## to get started
The following steps walk you through an easy, proven way of installing gbdxtools and its dependencies on Mac, Windows or Linux.


__1. Install Anaconda__
The first required step is to install Anaconda, an open source Python distribution that simplifies package management, dependencies, and environments (we recommend this step even if you already have a Python installation). This distribution includes Conda, which you will need in order to install gbdxtools using the provided conda environment file, and Jupyter Notebook, which you'll need to run the provided Jupyter Notebook that contains the gbdxtools tutorial.

1.1 Download and install the full version of [Anaconda](https://www.continuum.io/downloads)

Requirements:
- All users:
	- Python 2.7 version
		- *this will not interfere with other Python versions you may already have*
- Windows users:
	- 64-Bit is preferred
	- During the installation, please check the box that sets Path values when prompted
		- *please do this even though it is not the recommended setting*

__2. Install gbdxtools__

We have provided a Conda environment file for easy installion of gbdxtools within a virtual Python environment, along with its required dependencies. Virtual environments keep the dependencies required by different projects in separate places, so that they don't interfere with each other. Please use the following Conda commands to install gbdxtools.

Mac users:

2.1 Download the [gbdxtools_env.yml](../gbdxtools_module/gbdxtools_env.yml) file from this repo

2.2 Open a terminal window

2.3 Update conda
```
conda update conda
```
2.4 Create the conda environment
```
conda env create -f /full/path/to/gbdx_environment.yml
```
2.5 Activate the environment
```
source activate gbdxtools
```
2.6 Try importing all the modules (if no errors are raised, everything is working right)
```
python -c 'import rasterio; import fiona; import shapely; import gbdxtools'
```

Windows users:

2.1 Download the [gbdxtools_env.yml](../gbdxtools_module/gbdxtools_env.yml) file from this repo

2.2 Open cmd.exe

2.3 Update conda
```
conda update conda
```
2.4 Create the conda environment
```
conda env create -f C:\\full\path\to\gbdx_environment.yml
```
2.5 Activate the environment
```
activate gbdxtools
```
2.6 Try importing all the modules (if no errors are raised, everything is working right)
```
python -c 'import rasterio; import fiona; import shapely; import gbdxtools'
```

__3. Activate your GBDX acount credentials and locate your API key__ 

3.1 Activate your account - once you've been assigned to your company's GBDX account (we will do this for you, please coordinate with your company's GBDX POC), you'll be sent an email from DigitalGlobe with instructions on how to activate your account. Open the message and click on "ACTIVATE YOUR ACCOUNT". This will pop up a window where you will prompted to set a password.

3.2 Sign in to the [GBDX Web App](https://gbdx.geobigdata.io) with your GBDX username and password. 

3.3 Find your profile - first click the user icon in the lower left corner, then your username.

3.4 Look for the strings called “Client ID” and “Client Secret.” These are the GBDX credentials you'll need later to set up gbdxtools to interact with GBDX APIs.

__4. Start the Notebook tutorial__

Jupyter Notebook is an open-source web application that makes it easy to create and share documents - called Notebooks - that contain live code, equations, visualizations and explanatory text. When you start the app, it will launch a Python 'kernel' and the Notebook Dashboard from your browser. From here, you can open and close Notebooks and manage running kernels [(documentation here)](https://jupyter.readthedocs.io/en/latest/running.html#running). Use the following instructions to start the provided gbdxtools tutorial Notebook.

4.1 Download the file `gbdxtools-tutorial.ipynb` from this repository

4.2 Open a terminal/cmd window and navigate to the directory where you have saved gbdxtools-tutorial.ipynb

4.3 Start Jupyter Notebook
```
jupyter notebook
```
4.4 Click on gbdxtools-tutorial.ipynb to launch the Notebook.

4.5 The Notebook contains explanations of GBDX APIs and example code, which you can execute within the Notebook by selecting the cell and using the keyboard shortcut SHIFT + ENTER, or select the play button in the toolbar.

4.6 Within the Notebook itself, *Step 1.2* instructs you to enter your credentials to authenticate into GBDX. These are the email and password you used to sign up for GBDX, and the Client ID and Client Secret that you located in an earlier step. Enter these now and run this code cell to check that gbdxtools is installed correctly and that you have the correct credentials (if no errors are raised, everything is working right).

4.7 Follow the instructions in the notebook and optionally watch the [recording of this tutorial](https://digitalglobe.wistia.com/medias/u3tmwds3xo).

__5. Shut it down__

When you are finished with this tutorial, shut down the Jupyter Notebook and kernel, and deactivate the virtual Python environment where you installed gbdxtools.

5.1 Stop the jupyter notebook by using the keyboard shortcut `control + c`, then typing for `'y'` to confirm that you would like to shut down the notebook server.

Mac users:
5.2 Deactivate the virtual environment
```
source deactivate
```
5.3 (Optional) Remove the environment
```
conda remove --name gbdxtools --all
```

Windows users:
5.2 Deactivate the virtual environment
```
deactivate gbdxtools
```
5.3 (Optional) Remove the environment

```
conda remove --name gbdxtools --all
```
___
__6. Optional .gbdx-config file:__

Save a gbdxtools config file to your home directory with your GBDX credentials. This will allow you to authenticate a gbdxtools session without needing to enter your credentials each time.

6.1 You will need your GBDX credentials again (located within your profile information in the [GBDX Web App](https://gbdx.geobigdata.io/profile)).

6.2 Create a blank text file and copy and paste the following information:
    ```
    [gbdx]
    auth_url = https://geobigdata.io/auth/v1/oauth/token/
    client_id = <your_client_id>
    client_secret = <your_client_secret>
    user_name = <your_user_name>
    user_password = <your_password>
    ```
6.3 Replace `<your_client_id>` and `<your_client_secret>` with your credentials, also `<your_user_name>` and `<your_password>` with the username and password associated with your GBDX account.

6.4 Save this file in your home directory with the filename `.gbdx-config`
	- be sure to include the `.` at the beginning of the filename
	- the filename needs to be saved without an extension

6.5 Test your gbdxtools installation and config file:
	- Open a terminal/cmd window and type `python`
	- Copy and paste the following code, which will result in an error if it can't locate your config file or if the formatting is incorrect

   ```python
   from gbdxtools import Interface
   gbdx = Interface()
   ```
   - Once you are done, quit Python by typing `exit()`
<br/>

Config file troubleshooting:

Windows: select the filename and try to delete the '.txt' extension. You may need to save it as `.gbdx-config.` (notice the trailing period). Also, deselect the 'hide extensions' setting on your computer so you can verify if you've successfully deleted the extension.

Mac: select the config file, right-click and select 'Get Info' to verify that you've saved the file without an extension.

___




We would love to hear your feedback. Feel free to email GBDX-support@digitalglobe.com with comments and suggestions.
