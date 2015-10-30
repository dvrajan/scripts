#!/usr/bin/env python

import sys, gpxpy, getopt, datetime

def modify_time(input_file):
  gpx_file = open(input_file)
  gpx = gpxpy.parse(gpx_file)
  time = datetime.datetime.now()
  new_waypoints = []

  for waypoint in gpx.waypoints:
      time = time + datetime.timedelta(seconds=1)
      waypoint.time = time
      new_waypoints.append(waypoint)
  return new_waypoints

def write_to_gpx(waypoints, output_file):
    gpx = gpxpy.gpx.GPX()
    gpx.waypoints = waypoints
    print gpx.to_xml()  
    out_file = open(output_file, 'w')
    out_file.write(gpx.to_xml())
      
def print_usage():
    print 'gpx_time_generator.py -i <input_file> -o <output_file>'


def main(argv):
  inputfile = ''
  outputfile = 'out.gpx'
  try:
      opts, args = getopt.getopt(argv,"hi:o:",["help"])
  except getopt.GetoptError:
    print_usage()
    sys.exit(2)
  for opt, arg in opts:
      if opt == '-i':
          inputfile = arg
      elif opt == '-o':
          outpufile = arg
      elif opt in ('-h', '--help'):
          print_usage()
  waypoints = modify_time(inputfile)
  write_to_gpx(waypoints, outputfile)

if __name__ == "__main__":
  main(sys.argv[1:])
