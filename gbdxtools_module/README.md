## intro
GBDXtools is a GBDX Python package that allows one to easily access GBDX APIs to search the DigitalGlobe catalog, and order and process imagery. If you've completed any of the GBDX Notebooks tutorials, then you've seen gbdxtools in action. An important thing to know is that once you've installed gbdxtools locally, you can write and run analysis code in your local Python environment exactly as you would in GBDX Notebooks. 

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

__2.2__ Start Anaconda Prompt

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

### 3. Activate your GBDX acount credentials

__3.1__ Activate your account - once you've been assigned to your company's GBDX account (we will do this for you, please coordinate with your company's GBDX POC), you'll be sent an email from DigitalGlobe with instructions on how to activate your account. Open the message and click on "ACTIVATE YOUR ACCOUNT". This will pop up a window where you will prompted to set a password.

### 4. Test your gbdxtools installation

You can start Python from the gbdxtools environment, copy and paste the following code, and fill in your GBDX credentials. You will know that you've successfully installed gbdxtools if there's no error and it prints your GBDX S3 information. 

```python
import gbdxtools
gbdx = gbdxtools.Interface(
    username='',
    password=''
    )
    
gbdx.s3.info
```

From here, you can code against DigitalGlobe imagery using gbdxtools just as you did in the GBDX Notebooks tutorials, using the exact same gbdxtools commands.  

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
deactivate
```
__5.3__ (Optional) Remove the environment

```
conda remove --name gbdxtools --all
```
___
__6. Optional .gbdx-config file:__

It is recommended that you save your GBDX credentials in a config file, which is safer and more convenient than coding in your GBDX credentials. 

__6.1__ Create a blank text file and copy and paste the following information:
```
[gbdx]
user_name = <your_user_name>
user_password = <your_password>
```

__6.2__ Replace `<your_user_name>` and `<your_password>` with the username (email) and password associated with your GBDX account.

__6.3__ Save this file in your user directory with the filename `.gbdx-config`
	- be sure to include the `.` at the beginning of the filename
	- the filename needs to be saved without an extension

__Mac users__:
Typing `cd ~` in the terminal will take to your user directory, place your config file here. 

__Windows users__:
Typing `echo %USERPROFILE%` will print out the user directory, place your config file here.

__6.4__ Test your gbdxtools installation and config file:
	- Open a terminal/cmd window and type `ipython`
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
