#!/usr/bin/python

##########################################################################################
#
#  search_catalog_GBDX.py
#
#  Created by: Dave Loomis
#              Digitalglobe GBD Solutions
#
#  Version 0.1: Nov 29, 2016
#               - example of search of the gbd catalog with gbdxtools, and output shp
#                 of the catids
#
#  Usage: python search_catalog_GBDX.py outfile
#
#############################################################################################

from shapely.geometry import mapping
from shapely.wkt import loads
from fiona import collection
from fiona.crs import from_epsg
import fiona
import requests
#import json
import sys
from gbdxtools import Interface
gbdx = Interface()

# get the name of the file from the command line args
search_output = sys.argv[1]

wkt_string = "POLYGON ((130.48737 33.19963,130.92407 33.19963,130.92407 32.72722,130.48737 32.72722,130.48737 33.19963))"
filters = [ "cloudCover < 30 ",
             "offNadirAngle < 30 ",
             "(sensorPlatformName = 'WORLDVIEW02' OR sensorPlatformName ='WORLDVIEW03')"
           ]
results = gbdx.catalog.search(searchAreaWkt=wkt_string,
                           startDate="2015-12-01T00:00:00.000Z",
                           endDate="2016-12-01T00:00:00.000Z",
                           filters=filters)

r_dict = []
for r in results :
    # put the results into a dictionary to insert into shapefile later
    r_dict.append({"catid" : r["identifier"],
                   "cc" : r['properties']["cloudCover"],
                   "ona" : r['properties']["offNadirAngle"],
                   "browse" : r['properties']["browseURL"],
                   "acquisition" : str(r['properties']["timestamp"]).split("T")[0],
                   "geom" : r['properties']['footprintWkt']})

    # print the catalog id out to screen for testing
    print
    print r["identifier"]
    print "cloudcover:  " + r['properties']["cloudCover"]
    print "off nadir:   " + r['properties']["offNadirAngle"]
    print "browse url:  " + r['properties']["browseURL"]
    print "image bands:  " + r['properties']["imageBands"]
    print "acquisition: " + str(r['properties']["timestamp"]).split("T")[0]
    print "geom:        " + r['properties']["footprintWkt"]
    print
    print "------------------------------------------------"

# write the shapefile with fiona
out_file = "/home/<YOUR_DIRECTORY>/<SUBDIRECTORY>/" + search_output.replace(".shp","") + ".shp"

# build the catid shp file schema
schema = {'geometry': 'Polygon',
          'properties': {'catid' : 'str',
                         'cc':'str',
                         'ona' : 'str',
                         'browse' : 'str',
                         'acq_date' : 'str'}}
# build the catid shapefile
with fiona.open(out_file, 'w',crs=from_epsg(4326),driver='ESRI Shapefile', schema=schema) as output:
    for d in r_dict :
        geometry = loads(d["geom"])
        output.write({'properties':{'catid': d['catid'],
                                    'cc': d['cc'],
                                    'ona' : d['ona'],
                                    'browse' : d['browse'],
                                    'acq_date' : d['acquisition']
                                    },
                      'geometry': mapping(geometry)})

# show total number of results found
print
print "================================================="
print "Number of results returned:"
print len(results)
print "================================================="
print
