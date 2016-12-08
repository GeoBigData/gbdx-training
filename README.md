# TO-DO in preparation for GBDX Training

## GBDX Credentials
Please email GBDX-Support@digitalglobe.com for credentials or sign up for a free evaluation account via the [GBDX Web App](https://gbdx.geobigdata.io/login) and ensure that your credentials allow you to successfully log in

## Postman
Postman is a HTTP client that allows you to test API requests and create collections of frequently-used requests. Follow the instructions from [this GBDX University tutorial](http://gbdxdocs.digitalglobe.com/docs/postman-instructions-collections) to install Postman, set up your environment, and import GBDX postman collections

## gbdxtools  

gbdxtools is a pip-installable python package that allows one to easily access GBDX APIs to search the DigitalGlobe catalog, and order and process imagery

[Python](https://www.python.org/) and [Pip](https://pip.pypa.io/en/stable/installing/) are required to install gbdxtools. Alternatively, the [Anaconda](https://jupyter.readthedocs.io/en/latest/install.html) distribution installs Python, Pip, Jupyter, and IPython. By installing Anaconda, you will have the option to follow the gbdxtools demo through a provided Jupyter Notebook. Sample python code, however, will also be provided

gbdxtools is easy to install via pip
'''
pip install gbdxtools
'''
Following installation, store a configuration file containing your GBDX credentials to your root drive with the following format
'''
[gbdx]
auth_url = https://geobigdata.io/auth/v1/oauth/token/
client_id = your_client_id
client_secret = your_client_secret
user_name = your_user_name
user_password = your_password
'''


Follow the instructions provided in the [gbdxtools documentation](http://gbdxtools.readthedocs.io) to install gbdxtools. 

Once Python and Pip are installed, install gbdxtools installation instruction from gbdxtool documentation. The gbdxtools documentation includes instructions on how to use pip to install gbdxtools and set up a config file with your gbdx credentials to authenticate your gbdxtools session. Your GBDX credentials can be found in your user profile information within the [GBDX Web App](https://gbdx.geobigdata.io/login). After installation and config file setup, it is recommended that you start a python session with the following code
  '''
  from gbdxtools import Interface
  gbdx = Interface()
  '''
If gbdxtools and the config file are correctly set up, this code will instantiate a gbdx Interface object, which you will likely want to do every time you use gbdxtools. If you receive a config file error, please review the instructions. Common problems include formatting mistakes introduced from copy/paste, a config file extension, and/or not saving your config file to your home drive. 
