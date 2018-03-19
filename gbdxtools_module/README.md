## intro
GBDXtools is a GBDX Python package that allows one to easily access GBDX APIs to search the DigitalGlobe catalog, and order and process imagery. If you've completed any of the GBDX Notebooks tutorials, then you've seen gbdxtools in action. In this tutorial, we provide a easy method of installing gbdxtools in your local dev environment. 

## to get started

### 1. Install Anaconda

The first required step is to install Anaconda, an open source Python distribution that simplifies package management, dependencies, and environments (we recommend this step even if you already have a Python installation). This distribution includes Conda, which you will need in order to install gbdxtools using the provided conda environment file. 

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

### 2. Install gbdxtools

We have provided a Conda environment file for easy installion of gbdxtools, along with its required dependencies, within a Conda virtual environment. Virtual environments keep the dependencies required by different projects in separate places, so that they don't interfere with each other. Please use the following Conda commands to install gbdxtools.

__Mac users__:

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

__Windows users__:

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

### 3. Activate your GBDX acount credentials and locate your API key

__3.1__ Activate your account - once you've been assigned to your company's GBDX account (we will do this for you, please coordinate with your company's GBDX POC), you'll be sent an email from DigitalGlobe with instructions on how to activate your account. Open the message and click on "ACTIVATE YOUR ACCOUNT". This will pop up a window where you will prompted to set a password.

__3.2__ Sign in to the [GBDX Web App](https://gbdx.geobigdata.io) with your GBDX username and password.

__3.3__ Find your profile - first click the user icon in the lower left corner, then your username.

__3.4__ Look for the strings called “Client ID” and “Client Secret.” These are the GBDX credentials you'll need later to set up gbdxtools to interact with GBDX APIs.

### 4a. Test your gbdxtools installation

You can start Python from the gbdxtools environment, copy and paste the following code, and fill in your GBDX credentials. You will know that you've successfully installed gbdxtools if there's no error and it prints your GBDX S3 information. 

```python
import gbdxtools
gbdx = gbdxtools.Interface(
    username='',
    password='',
    client_id='',
    client_secret='')
    
gbdx.s3.info
```

From here, you can code against DigitalGlobe imagery using gbdxtools just as you did in the GBDX Notebooks tutorials, using the exact same gbdxtools commands.  

### 4b. Test your gbdxtools installation in a Jupyter Notebook

We provided the same code for testing your gbdxtools installation in a Jupyter Notebook, if this is more convenient for you. If you've completed any of the GBDX Notebooks tutorials, then you'll be familiar with this layout.

Jupyter Notebook is an open-source web application that makes it easy to create and share documents - called notebooks - that contain live code and explanatory text. Starting the Jupyter Notebook app will launch a Python 'kernel' and Notebook Dashboard in a browser window. From here, you can open and close notebooks and manage running kernels [(documentation here)](https://jupyter.readthedocs.io/en/latest/running.html#running). Use the following instructions to start the provided gbdxtools test notebook.

__4.1__ Download the file [gbdxtools-test.ipynb](../gbdxtools_module/gbdxtools-test.ipynb) from this repository

__4.2__ Go back to the terminal window where you have activated the gbdxtools environment and navigate to the directory where you have saved gbdxtools-test.ipynb

__4.3__ Start the Jupyter Notebook App by typing the following command in the terminal
```
jupyter notebook
```
__4.4__ Click gbdxtools-test.ipynb to launch the notebook.

__4.5__ Switch to the gbdxtools environment kernel:
- select the "Kernel" dropdown menu from the toolbar
- hover over "Change Kernel"
- select Python [conda env:gbdxtools]

__4.6__ Use the Shift-Return ⇧↩︎ keyboard shortcut to execute code within a cell. The first code cell will ouput your Python instance.

__4.7__ In the Notebook - *Step 1.2* instructs you to enter your credentials to authenticate into GBDX. These are the email and password you used to sign up for GBDX, and the Client ID and Client Secret that you located in step 3. Enter these now and run this code cell to check that gbdxtools is successfully installed and that you have valid credentials (if no errors are raised, everything is working correctly).

### 5. Shut it down

When you are finished with this tutorial, shut down the Jupyter Notebook and kernel, and deactivate the Conda environment where you installed gbdxtools.

__5.1__ Stop the jupyter notebook by using the keyboard shortcut `CONTROL + C`, then `'Y'` to confirm that you would like to shut down the notebook server.

__Mac users__:

__5.2__ Deactivate the virtual environment
```
source deactivate
```
__5.3__ (Optional) Remove the environment
```
conda remove --name gbdxtools --all
```

__Windows users__:

__5.2__ Deactivate the virtual environment
```
deactivate gbdxtools
```
__5.3__ (Optional) Remove the environment

```
conda remove --name gbdxtools --all
```
___
__6. Optional .gbdx-config file:__

Save a gbdxtools config file to your home directory with your GBDX credentials. This will allow you to authenticate a gbdxtools session without needing to enter your credentials each time.

__6.1__ You will need your GBDX credentials again (located within your profile information in the [GBDX Web App](https://gbdx.geobigdata.io/profile)).

__6.2__ Create a blank text file and copy and paste the following information:
```
[gbdx]
auth_url = https://geobigdata.io/auth/v1/oauth/token/
client_id = <your_client_id>
client_secret = <your_client_secret>
user_name = <your_user_name>
user_password = <your_password>
```

__6.3__ Replace `<your_client_id>` and `<your_client_secret>` with your credentials, also `<your_user_name>` and `<your_password>` with the username and password associated with your GBDX account.

__6.4__ Save this file in your home directory with the filename `.gbdx-config`
	- be sure to include the `.` at the beginning of the filename
	- the filename needs to be saved without an extension

__6.5__ Test your gbdxtools installation and config file:
	- Open a terminal/cmd window and type `python`
	- Copy and paste the following code, which will result in an error if it can't locate your config file or if the formatting is incorrect.

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
