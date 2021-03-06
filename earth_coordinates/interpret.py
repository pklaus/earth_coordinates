#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philippklaus.de

from .coordinates import Coordinates, Latitude, Longitude
import re

NUMBER = u"([0-9]{1,3}(\\.[0-9]{1,9})?)" # regex for a number (such as 999, 12.12 0.000000001)
NUMBER60 = u"[\+-]?[0-5]?[0-9]" # regex for a pos./neg. number up to 59 (such as -59, 0, 22)
NUMBER60_DEC = NUMBER60 + u"(\\.[0-9]{1,9})?" # regex for a pos/neg with abs(number)<60 with up to 9 decimals
NUMBER60_DEC_G = u"(?P<%s>" + NUMBER60_DEC + u")" # create named regex from regex above (replace the placeholder %s with the name)
NUMBER360 = u"[\+-]?(35[0-9]|3[0-4][0-9]|[1-2][0-9][0-9]|0?[0-9]?[0-9])" # regex for pos/neg integer degree values with abs(number)<360 (such as -359, 002, 1, 099)
NUMBER360_DEC = NUMBER360 + u"(\\.[0-9]{1,9})?" # above regex with an optional addition of up to 9 digits 
NUMBER360_DEC_G = u"(?P<%s>" + NUMBER360_DEC + u")" # create named regex from regex above (replace the placeholder %s with the name)
SPACE = u"\\s{1,5}" # the maximum number of spaces between text elements in the angle strings
DEG_ANGLE = (NUMBER360_DEC_G % "degrees") + u"\u00B0?" # U+00B0 is the degree sign °
DEG_MIN_ANGLE = DEG_ANGLE + SPACE + (NUMBER60_DEC_G % 'minutes') + u"'?"
DEG_MIN_SEC_ANGLE = DEG_MIN_ANGLE + SPACE + (NUMBER60_DEC_G % 'seconds') + u"\"?"

LATITUDE_NAME  = r"[nNsS][\. ]?(lat\.?)?"
LONGITUDE_NAME = r"[eEwW][\. ]?(lon\.?)?"

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
    latitude = interpret_angle(lat_string, True)
    longitude = interpret_angle(lon_string, False)
    return Coordinates(latitude, longitude)

def interpret_angle(angle_string, should_be_latitude=True):
    angle_string = angle_string.strip()
    match = re.search(DEG_MIN_SEC_ANGLE, angle_string)
    value = None
    if match != None:
        degs, mins, secs = match.group('degrees'), match.group('minutes'), match.group('seconds')
        value = float(degs)+float(mins)/60.0+float(secs)/60.0**2
    if value == None:
        match = re.search(DEG_MIN_ANGLE, angle_string)
        if match != None:
            degs, mins = match.group('degrees'), match.group('minutes')
            value = float(degs)+float(mins)/60.0
    if value == None:
        match = re.search(DEG_ANGLE, angle_string)
        if match != None:
            degs = match.group('degrees')
            value = float(degs)
    if value != None:
        match_latitude = re.search(LATITUDE_NAME, angle_string)
        match_longitude = re.search(LONGITUDE_NAME, angle_string)
        if match_latitude != None:
            return Latitude(value)
        if match_longitude != None:
            return Longitude(value)
        if should_be_latitude:
            return Latitude(value)
        else:
            return Longitude(value)
    raise CoordinateInterpretationError(angle_string, "Trying to interpret %s" % angle_string)
