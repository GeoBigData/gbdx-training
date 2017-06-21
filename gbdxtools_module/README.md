## intro 
GBDXtools is a pip-installable Python package that allows one to easily access GBDX APIs to search the DigitalGlobe catalog, and order and process imagery. 

## what you will learn 
In this tutorial, we'll demonstrate how to search the DigitalGlobe archive via the Catalog API, order imagery using the Order API, and run an analysis workflow with the Workflow API. 

## to get started
__Activate your GBDX acount credentials and locate your API key

Before we start, you'll need your GBDX username, password, and API key. 

1. Activate your account - once you've been assigned to your company's GBDX account (we will do this for you, please coordinate with your company's GBDX POC), you'll be sent an email from DigitalGlobe with instructions on how to activate your account. Open the message and click on "Confirm my account." An account confirmation will appear. Now you're ready to start using GBDX.

2. Sign in to the [GBDX Web App](https://gbdx.geobigdata.io) with your GBDX username and password.

3. Find your profile - first click the user icon in the lower left corner, then your username.

4. Look for the strings called “Client ID” and “Client Secret.” These are the GBDX credentials you'll need later to set up gbdxtools to interact with GBDX APIs.

__Install Anaconda and gbdxtools:__ 

Pre-requisites for installing gbdxtools are Python and Pip. However, we recommend that you first install Anaconda, an open source Python distribution that simplifies package management, this will install Python and Pip for you. The Anaconda install also includes Jupyter, which you will need if you choose to use the provided Jupyter Notebook for this tutorial. 

1. Install Anaconda: Download and install Anaconda from https://www.continuum.io/downloads, and be sure to check the box that sets Path values when prompted.

2. Install gbdxtools 
- Mac/Linux: Open a terminal window, and copy and paste the following commands [(troubleshooting tips)](https://github.com/DigitalGlobe/gbdxtools): <br/>
`pip install gbdxtools` <br/>
`pip install gbdx-auth`

- Windows: Follow the directions for installing gbdxtools on Windows [here](https://github.com/DigitalGlobe/gbdxtools/blob/master/install_windows.md)

__Download and start the Notebook tutorial:__
1. Download the file gbdxtools-tutorial.ipynb from this repository

2. Open a terminal/cmd window and copy and paste `jupyter notebook`. This will open the Jupyter Notebook interface in your browser [(documentation here)](https://jupyter.readthedocs.io/en/latest/running.html#running). 

3. Within in the Jupyter Notebook interface, navigate to where you saved the gbdxtools-tutorials.ipynb file and click on it to start the notebook. 

4. The gbdxtools-tutorial.ipynb contains explanations of the APIs and example code, which you can execute within the notebook by selecting the cell and using the keyboard shortcut SHIFT + ENTER, or select the play button in the toolbar. Follow the instructions in the notebook and optionally watch the [recording of this tutorial](https://digitalglobe.wistia.com/medias/u3tmwds3xo). 
 
__Optional .gbdx-config file:__

Save a gbdxtools config file to your home directory with your GBDX credentials. This will allow you to authenticate a gbdxtools session without needing to hard code your credentials every time you want to use gbdxtools.   

1. You will need your GBDX credentials again (located within your profile information in the [GBDX Web App](https://gbdx.geobigdata.io)).

2. Create a blank text file and copy and paste the following information:
    ```
    [gbdx]
    auth_url = https://geobigdata.io/auth/v1/oauth/token/
    client_id = <your_client_id>
    client_secret = <your_client_secret>
    user_name = <your_user_name>
    user_password = <your_password>
    ```
3. Replace `<your_client_id>` and `<your_client_secret>` with your credentials, also `<your_user_name>` and `<your_password>` with the username and password associated with your GBDX account. 

4. Save this file in your home directory with the filename `.gbdx-config`. Two things of note - be sure to include the '.' at the beginning of the filename, and be sure that the filename is saved without an extension. 

5. Test your gbdxtools installation: Open a terminal/cmd window and type `python`. Then copy and paste the following code, which will result in an error if gbdxtools is not properly installed. Once you are done, quit Python by typing `exit`. 

   ```python
   from gbdxtools import Interface
   gbdx = Interface()
   ```
<br/>

__Config file troubleshooting:__

Windows: try to select the filename and delete the '.txt' extensions. You may need to save it as `.gbdx-config.` (notice the extra period at the end of the filename) and/or change the 'hide extensions' setting on your computer so you can verify if you've successfully deleted the extension. 

Mac: select the config file, right-click and select 'Get Info' to verify that you've saved the file without an extension. 

___
We would love to hear your feedback. Feel free to email GBDX-support@digitalglobe.com with comments and suggestions.
