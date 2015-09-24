#!/bin/bash
# Converts the GPX with <trkpt> elements to GPX with <wpt> elements.
# Also removes <trk> and <trkseg> elements

# GPX with <wpt> elements is used to simulate locations with XCode for iOS

if [ $# -le 1 ]
then    
    echo "Usage: convert_gpx.sh <input_gpx_file> <output_gpx_file>"
    exit 1
fi

sed 's/trkpt/wpt/g
/trkseg/d
/trk/d' <  $1 > $2
