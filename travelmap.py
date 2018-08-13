

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory, which contains .md files of all your talks. 
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: glob, getorg, geopy

import glob
import getorg
from geopy import Nominatim


geocoder = Nominatim()
location_dict = {}
locations = ['Berkeley, California, USA',
             'San Francisco, California, USA',
             'Seattle, Washington, USA',
             'San Diego, California, USA',
             'Salt Lake City, USA',
            ]
permalink = ""
title = ""


for loc in locations:                                   
    location_dict[loc] = geocoder.geocode(loc)
    print(loc, "\n", location_dict[loc])

m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="travelmap", hashed_usernames=False)
