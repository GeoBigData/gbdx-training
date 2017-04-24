# Preparation for GBDX Training
DigitalGlobe's GBDX platform provides customers with a fast and easy way to search, order, and process DigitalGlobe images as well as their own data. In this training, we will be concentrating on providing information to enhance your knowledge of GBDX APIs. While there are multiple ways to interact with GBDX APIs, in this tutorial we will focus on Postman- an HTTP client for testing web services, and gbdxtools- a Python SDK for accessing GBDX APIs. 

### Sign up for GBDX and locate your account credentials
Before we start, you'll need your GBDX username, password, and API key.  

1. Sign up for GBDX - if you're new to GBDX, you'll need to create an account. If you received an email invitation to GBDX from your company, follow the instructions to create your user account. Otherwise, start here-

2. Go to the [GBDX home page](https://gbdx.geobigdata.io/login).

3. Select "Sign up" from the login box. Enter the email name and password you want to use for this account, then click "SIGN UP."

4. Fill in your personal information and account information. Choose "Register GBDX Account."

5. Activate your account - after you register, you'll get an email message from DigitalGlobe asking you to activate your account. Open the message and click on "Confirm my account." An account confirmation will appear. Now you're ready to start using the web application.

6. Sign in to the [GBDX Web App](https://gbdx.geobigdata.io) with your GBDX username and password.

7. Find your profile - first click the user icon in the lower left corner, then your username.

8. Look for the strings called “Client ID” and “Client Secret.” These are the GBDX credentials you'll need later to set up Postman and gbdxtools to interact with GBDX APIs.


### Install gbdxtools
gbdxtools is a pip-installable python package that allows one to easily access GBDX APIs to search the DigitalGlobe catalog, and order and process imagery. Pre-requisites for installing gbdxtools are Python and Pip. However, we recommend that you first install Anaconda, an open source Python distribution that simplifies package management, which will install Python and Pip for you. The Anaconda install also includes Jupyter, which will be very handy during hands-on tutorials. We use Jupyter Notebooks extensively for GBDX demos. 

1. Install Anaconda: Download and install Anaconda from https://www.continuum.io/downloads, and be sure to check the box that sets Path values when prompted.

2. Install gbdxtools: Open a terminal (Mac) or cmd (Windows) window, and copy and paste the following commands [(troubleshooting tips)](https://github.com/DigitalGlobe/gbdxtools): <br/>
`pip install gbdxtools` <br/>
`pip install gbdx-auth`

3. Create config file: All operations on GBDX require credentials. gbdxtools expects a config file to exist at ~/.gbdx-config with your GBDX credentials. Your credentials are listed in https://gbdx.geobigdata.io/profile. <br/> Create the file `~/.gbdx-config` (no extension!), include the following information, and save it to your home directory. 
    
    ```
    [gbdx]
    auth_url = https://geobigdata.io/auth/v1/oauth/token/
    client_id = <your_client_id>
    client_secret = <your_client_secret>
    user_name = <your_user_name>
    user_password = <your_password>
    ```

4. Test your gbdxtools installation: Open a terminal/cmd window and type `python`. Then copy and paste the following code, which will result in an error if gbdxtools is not properly installed. Once you are done, quit Python by typing `exit`. 

   ```python
   from gbdxtools import Interface
   gbdx = Interface()
   ```
 
6. Test Jupyter: Open a terminal/cmd window and copy and paste the following code to test that Jupyter is installed. This will open the Jupyter Notebook interface in your browser [(documentation here)](https://jupyter.readthedocs.io/en/latest/running.html#running): <br/>
`jupyter notebook`
 
7. If you would like to explore gbdxtools and Jupyter Notebooks, download 'gbdxtools-APIs.ipynb' from this repo and open it in the Jupyter Notebook browser interface. This interface should just open when you start the Jupyter server, but if not, simply open the following URL in a browser: http://localhost:8888 [Documentation (https://jupyter.readthedocs.io/en/latest/running.html#running)

### Install Docker and register for a Docker Hub account
The platform utilizes the Docker technology to bundle algorithms and their dependent code into docker images that can be registered as tasks on the platform. 

1. Browse to [Docker Hub](hub.docker.com) to create a Docker Hub account.

2. Download and install the [Docker client](https://www.docker.com).

3. Test your installation - open a terminal/cmd window and copy and paste the following command. This should output info about your Docker installation.

    ```
    docker --version
    ```

### Install Postman, download GBDX Training Collection for Postman and Import
The Postman client lets you test API requests and create collections of frequently-used requests.

1. Get postman: http://getpostman.com

2. Download GBDX Postman files from the [GBDX Github location](https://github.com/TDG-Platform/postman).

3. Click "Download zip". You'll find it above the file list. It will save a zip file called Postman_Master to your local machine.

4. Find the zip file on your local machine and unzip it.

5. Open the Postman_Master file and check to make sure the following files are there. You'll need them when you set up Postman.

    Environment file: GBDX.postman_environment
    Collection file: GBDX.json.postman_collection

6. Set up your GBDX environment.

    select the environment pull down menu
    choose "manage environments" 
    select "choose files"
    navigate to the file location where you saved the Postman files
    select and open the file "GBDX.postman_environment" to import it 

7. Enter your environment variables.

    choose the Back button
    select "GBDX"
    enter your GBDX username, password, and API key (you already located info this from your Web App profile)
    
8. Make sure "GBDX" is selected from the dropdown menu in the top right corner.

9. Import the GBDX Collections.

    choose "import" from the top of the screen
    navigate to the file location where you saved the file "GBDX.json.postman_collection" and select it
    
10. Get a token.

    on the left hand side under Collections, click "GBDX"
    under "Auth" select the Post "Get User Token"
    you've already added your environment variables, so you can simly click Send
    copy your "access_token" from the response body and add to the GBDX environment variables (check step 7)
      *this token is valid for seven days, after which you will need to repeat this step


### Resources <br />
GBDX Jupyter Notebooks
https://juno.timbr.io/hub/notebooks

GBDX Web App <br />
https://gbdx.geobigdata.io 


GBDX University <br />
http://gbdxdocs.digitalglobe.com


gbdxtools Documentation <br />
http://gbdxtools.readthedocs.io 


gbdxtools Github <br />
https://github.com/DigitalGlobe/gbdxtools


s3 browser <br />
http://s3browser.geobigdata.io


Postman <br />
https://www.getpostman.com


Docker <br />
https://www.docker.com


Dockerhub <br />
https://hub.docker.com

Anaconda <br />
https://docs.continuum.io/anaconda/install

Jupyter <br />
http://jupyter.org


Python <br />
https://www.python.org


Pip <br />
https://pip.pypa.io


JSON Lint <br />
http://jsonlint.com


App that reads and writes Well-Known Text (WKT) strings <br />
http://arthur-e.github.io/Wicket/sandbox-gmaps3.html


Testing a docker image <br />
http://gbdxstories.digitalglobe.com/create-task/#registering-a-task-on-gbdx


Task-to-GBDX tutorials <br />
http://gbdxstories.digitalglobe.com/create-task <br/>
https://github.com/GeoBigData/Taskifying





  
