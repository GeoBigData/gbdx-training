### Create a project
1. SIGN INTO ANSWERFACTORY<br/>
Sign into AnswerFactory using your GBDX credentials. This will be the email address and password you created for your GBDX account. 

2. CREATE A NEW PROJECT<br/>
Click on the "New Project" button at the top of the page. This will take you to the Create New Project homepage with the Project Information Panel to the left of the screen.

3. ADD AN AREA OF INTEREST (AOI)<br/>
We have provided a shapefile over Shanghai Hongqiao International Airport for this tutorial. If you haven't done so already, please download the "SHA.zip" file from this github repo. <br/> <br/> Upload this shapefile to AnswerFactory by clicking on the "Upload Shapefile" button in the Project Panel and selecting the zipped file. The map wil snap to the AOI defined by the shapefile, and you will see more configurable options in the Project Panel.  

4. NAME YOUR PROJECT<br/>
For this tutorial, give your project a unique name by naming it something like, "extract_aircraft" and attach your initials at the end. This name will be checked against existing names to prevent multiple projects from having the same name. 

5. ADD THE 'EXTRACT AIRCRAFT 'ANSWER TO YOUR PROJECT<br/>
For this demo, you are going to run the AnswerFactory 'Extract Aircraft' recipe. This recipe runs an algorithm over an image to identify aircraft and generate vectors that indicate where the aircraft are. There are three subtypes of aircraft currently being detected: Airliner, Fighter, and Helicopter. <br/> <br/> Click on the Add Answers button to bring up the modal for selecting answers. Click in the field to open the dropdown list of currently available answers. Choose the 'Extract Aircraft' selection at the top of the list, which will pop up in a panel on the right side of your screen. 

6. SAVE PROJECT<br/>
Click on the Create Project button at the bottom of the Project Panel. When prompted, confirm that you want to create the project. <br/> <br/> At this point, the analysis has begun. You should see a message on the right side of the screen that states, "Currently running Extract Aircraft'.

### Check results in the App
Normally, it would take some time for the algorithm to process and return the results. However, AnswerFactory is smart and won't process the same algorithm over the same image twice, but will instead query and provide the vector output that already exists. This is what will happen when you run the 'Extract Aircraft' recipe over the AOI you defined using the provided shapefile. Instead of waiting for AnswerFactory to process new results, you will receive an 'Answer Ready!' email within a couple hours. You can follow the link within the email or follow the instructions outlined below to view your completed project.

1. OPEN YOUR PROJECT<br/>
Click on the 'Open Project' button at the top of the screen. This will bring up the projects list on the left side of the page, where you can browse a list of public projects. To find your project, check the toggle for 'Show Only My Projects', then select your unique "extract_aircraft" project. <br/> <br/> You will be presented with the base View Project page for your project, which contains the Project Information Panel to the left and the Answer List to the right. Note that the Project Details section contains all of the information found when you created the project, along with additional information about the project owner, the date and time of project creation, and the date and time that the project was last modified. The Answers Panel on the right shows all of the answers that have been run for the project. 

2. VIEW AN ANSWER<br/> 
In the Answer Panel, click on the 'Extract Aircraft' text. A table will appear on the bottom half of the screen. The table will display a row for each AOI. The columns to the right of the Name column are labeled with the acquisition dates of the images that the answer was run against. For each of the acquisitions, you will find statistics stating the number of vectors found, the vector coverage percentage within the AOI, and the image coverage percentage within the AOI. <br/> <br/> Select a cell under its acquisition date to load the vector results and source imagery used for the analysis. Hover over the blue dot icon in the upper right corner to see the map table of contents. Click the first layer, "Extract Aircraft" to toggle on/off the vector results. Clicking the layer that begins with a catalog ID (ex. 104001002979E100) will toggle on/off the source imagery used in the analysis.  

3. DIG INTO AN ANSWER<br/>
Double click on one of the cells to load a table of the individual vectors for that cell. Click the magnifying glass next to a row to pan/zoom to that specific vector.

### View results in a GIS 
You can also download the vector output from your analysis for use outside of the app. In this part of the tutorial, we are going to demonstrate how to download the output as GeoJSON and view it in a GIS. We'll show how to load the data into both QGIS and ArcMap. <br/> 

1. DOWNLOAD VECTOR OUTPUT<br/>
From the main table view, click on the "Download All Results" button at the bottom left, which will save the vector output in GeoJSON format to "openskynet-aircraft-detection.json". 

2. VIEW OUTPUT IN QGIS<br/>
From here, it is simple to view the vector output in QGIS. Open the QGIS application and start a new project. Locate the "openskynet-aircraft-detection.json" file in your Downloads folder, then simply drag and drop it into the QGIS main viewer window. The loaded data will display as polygons indicating where aircraft were found using the "Extract Aircraft" algorithm.  

