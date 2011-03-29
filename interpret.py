#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philippklaus.de

from coords import coords
import re

NUMBER = u"([0-9]{1,3}\\.?[0-9]{0,9})"
SPACE = u"\\s{1,5}" # the maximum number of spaces between text elements in the angle strings
DEG_ANGLE = NUMBER + u"\u00B0?" # U+00B0 is the degree sign °
DEG_MIN_ANGLE = DEG_ANGLE + SPACE + NUMBER + u"'?"
DEG_MIN_SEC_ANGLE = DEG_MIN_ANGLE + SPACE + NUMBER + u"\"?"

class CoordinateInterpretationError(Exception):
    pass

def interpret(coordinate_string):
    coordinate_string = coordinate_string.strip()
    lat_string, lon_string = None, None
    if coordinate_string.count(",") == 1: # If we find exactly one comma it might dividing the latitude form the longitude.
        fragments = coordinate_string.split(",")
        lat_string, lon_string = fragments[0], fragments[1]
    if not (lat_string and lon_string):
        raise CoordinateInterpretationError(coordinate_string, "Trying to interpret %s" % coordinate_string)
    latitude = interpret_angle(lat_string)
    longitude = interpret_angle(lon_string)
    return coords(latitude,longitude)

def interpret_angle(angle_string):
    angle_string = angle_string.strip()
    match = re.match(DEG_MIN_SEC_ANGLE,angle_string)
    #import pdb; pdb.set_trace()
    if match != None:
        #print "Found a notation with degrees, minutes and seconds."
        degs, mins, secs = match.groups()[0], match.groups()[1], match.groups()[2]
        return float(degs)+float(mins)/60.0+float(secs)/60.0**2
    match = re.match(DEG_MIN_ANGLE,angle_string)
    if match != None:
        #print "Found a notation with degrees and minutes."
        degs, mins = match.groups()[0], match.groups()[1]
        return float(degs)+float(mins)/60.0
    match = re.match(DEG_ANGLE,angle_string)
    if match != None:
        #print "Found a notation with decimal degrees."
        degs = match.groups()[0]
        return float(degs)
    else:
        raise CoordinateInterpretationError(angle_string, "Trying to interpret %s" % angle_string)

if __name__ == '__main__':
    while True:
        inp = raw_input("Enter Coordinates: ")
        try:
            coordinates = interpret(inp)
        except CoordinateInterpretationError:
            print "Sorry, I could not interpret your input."
            continue
        print coordinates
