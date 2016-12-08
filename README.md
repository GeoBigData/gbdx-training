# TO-DO in preparation for GBDX Training

## GBDX Credentials
Please email GBDX-Support@digitalglobe.com for credentials or sign up for a free evaluation account via the [GBDX Web App](https://gbdx.geobigdata.io/login) and ensure that your credentials allow you to successfully log in.

## Postman
Postman is a HTTP client that allows you to test API requests and create collections of frequently-used requests. Follow the instructions from [this GBDX University tutorial](http://gbdxdocs.digitalglobe.com/docs/postman-instructions-collections) to install Postman, set up your environment, and import GBDX postman collections.

## gbdxtools  

gbdxtools is a pip-installable python package that allows one to easily access GBDX APIs to search the DigitalGlobe catalog, and order and process imagery.

Install [Python](https://www.python.org/) and [Pip](https://pip.pypa.io/en/stable/installing/) before installing gbdxtools. Alternatively, the [Anaconda](https://jupyter.readthedocs.io/en/latest/install.html) distribution installs Python, Pip, Jupyter, and IPython. Installing Anaconda will allow you to learn gbdxtools through the provided Jupyter Notebook, although sample python code is also provided.

gbdxtools is easy to install via pip
  ```
  pip install gbdxtools
  ```

gbdxtools expects a config file to exist at ~.gbdx-config with your GBDX credentials, in the following format
  ```
  [gbdx]
  auth_url = https://geobigdata.io/auth/v1/oauth/token/
  client_id = your_client_id
  client_secret = your_client_secret
  user_name = your_user_name
  user_password = your_password
  ```
This information can be found in your user profile from the [GBDX Web App](https://gbdx.geobigdata.io/login). Documentation on gbdxtools installation and use can be found at http://gbdxtools.readthedocs.io/en/latest/index.html and https://github.com/DigitalGlobe/gbdxtools.

Ensure that the gbdxtools installation and your config file are working by starting a Python session with the following code
  ```
  from gbdxtools import Interface
  gbdx = Interface()
  ```
This will instantiate a gbdx Interface object, which is something you'll want to do each time you begin a gbdxtools session. Congratulations! You are now ready to explore GBDX. If you receive an error message, you may need to check your config file for copy/paste errors, that the file doesn't have an extension (it may be hidden), and/or make sure it is stored in your root directory.   
