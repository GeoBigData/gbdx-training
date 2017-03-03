#!/usr/bin/python

##########################################################################################
#
#  search_gbdx_catids_to_shp.py
#
#  Created by: Dave Loomis
#              Digitalglobe GBD Solutions
#
#  Version 0.1: Feb 8, 2017
#               - search catids and output shapefile
#
#  Usage: python search_gbdx_catids_to_shp.py outfile
#
#  This script will search the catalog with the given set of catids and
#    output a shapefile with all of the catids and their attributes
#
#  If you do not want to create a shapefile of the result
#    you can disable the "fiona" and "shapely" codes segments and just output
#    the search results in text format
#
#############################################################################################
from shapely.geometry import mapping
from shapely.wkt import loads
from fiona import collection
from fiona.crs import from_epsg
import fiona
import requests
import sys
from gbdxtools import Interface
gbdx = Interface()

# get the name of the file from the command line args
search_output = sys.argv[1]

# provide a list of catids
catids = ['1040010026263300',
'103001005DBC7F00',
'103001005A404C00',
'104001001C593D00',
'1030010005D85300']

# initialize the list of output attributes
r_dict = []
# loop through the catid list
for catid in catids :
  r = gbdx.catalog.get(catid)
  r_dict.append({"catid" : r["identifier"],
                   "cc" : r['properties']["cloudCover"],
                   "ona" : r['properties']["offNadirAngle"],
                   "browse" : r['properties']["browseURL"],
                   "acquisition" : str(r['properties']["timestamp"]).split("T")[0],
                   "geom" : r['properties']['footprintWkt']})

# set up the directory of the output file
out_file = "/home/<YOUR_DIRECTORY>/<SUBDIRECTORY>/" + search_output.replace(".shp","") + ".shp"

# build the catid shp file schema for the output shapefile
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
print "Shapefile written to : " + out_file
print "Number of results returned:"
print len(r_dict)
print "================================================="
print