#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philippklaus.de

MIN_LAT =  -90.0
MAX_LAT =   90.0
MIN_LON = -360.0
MAX_LON =  360.0

class AngleOutOfBounds(Exception):
    pass

class coordinates(object):
    def __init__(self,lat=0.0,lon=0.0):
        """lat and lon can be of type float or of type angle (as well as its subclasses longitude and latitude)"""
        if isinstance(lat, angle) and isinstance(lon, angle):
            self.lat = lat
            self.lon = lon
        else:
            self.lat = latitude(float(lat))
            self.lon = longitude(float(lon))

    def __cmp__(self, coords):
        if isinstance(coords, coordinates):
            if self.lat == coords.lat and self.lon == coords.lon:
                return 0
        return 1
    def __str__(self):
        return "%s, %s" % (self.lat, self.lon)
    def __repr__(self):
        return "coordinates: %r, %r" % (self.lat, self.lon)

class angle(object):
    def __init__(self,value=0.0):
        self.set(value)

    def set(self,value):
        self.value = value

    def __str__(self):
        return "%f" % self.value

    def __cmp__(self,other_angle):
        if isinstance(other_angle, angle):
            if self.value == other_angle.value:
                return 0
        return 1
    def __repr__(self):
        return "%r %f °" % (str(type(self)).split('.')[1].split("'")[0], self.value)

class latitude(angle):
    def set(self,value):
        if value < MIN_LAT or value > MAX_LAT:
            raise AngleOutOfBounds
        return super(latitude, self).set(value)
    
    def __cmp__(self,other_latitude):
        if isinstance(other_latitude, latitude):
            return super(latitude, self).__cmp__(other_latitude)
        return 1
class longitude(angle):
    def set(self,value):
        if value < MIN_LON or value > MAX_LON:
            raise AngleOutOfBounds
        return super(longitude, self).set(value)
    
    def __cmp__(self,other_longitude):
        if isinstance(other_longitude, longitude):
            return super(longitude, self).__cmp__(other_longitude)
        return 1

if __name__ == '__main__':
    pass
