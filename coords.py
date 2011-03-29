#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philippklaus.de


class coords(object):
    def __init__(self,lat=0.0,lon=0.0):
        self.lat=lat
        self.lon=lon

    def __cmp__(self, coordinates):
        if isinstance(coordinates, coords):            
            if self.lat == coordinates.lat and self.lon == coordinates.lon:
                return 0
        return 1
    def __str__(self):
        return "%f, %f" % (self.lat, self.lon)

if __name__ == '__main__':
    pass
