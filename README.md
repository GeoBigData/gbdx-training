# TO-DO in preparation for GBDX Training

## GBDX Credentials
If you do not already have a GBDX account through your organization, please email GBDX-Support@digitalglobe.com for credentials or sign up for a free evaluation account on the [GBDX Web App](https://gbdx.geobigdata.io/login) and check that your credentials allow you to log in

## Postman
Postman is a HTTP client that allows you to test API requests and create collections of frequently-used requests. Follow the instructions from [this GBDX University tutorial](http://gbdxdocs.digitalglobe.com/docs/postman-instructions-collections) on how to install Postman, set up your environment, and import GBDX postman collections

## gbdxtools (python/pip or anaconda) 

gbdxtools is a python wrapper (sdk?) for GBDX APIs that makes it easy to search the DigitalGlobe catalog, and order and process imagery. In order to install gbdxtools, [Python](https://www.python.org/) and [Pip](https://pip.pypa.io/en/stable/installing/) will need to be installed on your machine. 

(Alternatively, you can install the [Anaconda](https://jupyter.readthedocs.io/en/latest/install.html) distribution, which includes Python, Pip, and Jupyter, and IPython. Jupyter Notebook is an interactive computational environment that provides an easy way to demonstrate gbdxtools. By installing Anaconda, you will be able to follow the gbdxtools tutorial within the notebook, although python code sample will also be provided. IPython is (...better than python)

Once Python and Pip are installed, install gbdxtools installation instruction from gbdxtool documentation. The gbdxtools documentation includes instructions on how to use pip to install gbdxtools and set up a config file with your gbdx credentials to authenticate your gbdxtools session. Your GBDX credentials can be found in your user profile information within the [GBDX Web App](https://gbdx.geobigdata.io/login). After installation and config file setup, it is recommended that you start a python session with the following code
  '''
  from gbdxtools import Interface
  gbdx = Interface()
  '''
If gbdxtools and the config file are correctly set up, this code will instantiate a gbdx Interface object, which you will likely want to do every time you use gbdxtools. If you receive a config file error, please review the instructions. Common problems include formatting mistakes introduced from copy/paste, a config file extension, and/or not saving your config file to your home drive. 
