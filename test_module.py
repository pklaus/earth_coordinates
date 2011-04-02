#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philippklaus.de

import unittest
import random

import re
from interpret import DEG_MIN_SEC_ANGLE

from interpret import interpret, interpret_angle
from coordinates import coordinates, latitude

VALID_COORDINATE_SAMPLES = ( (  "20.123 N, 19.132 E", ( 20.123, 19.132)  )  ,
                             (  "20.123, 19.132",     ( 20.123, 19.132)  )  ,
                             (  "N20.123, E19.132",   ( 20.123, 19.132)  )  ,
                           )

class test_coordinates(unittest.TestCase):

    def test_interpret(self):
        self.assertEqual(interpret("11,10"),coordinates(11,10))
        
        sample_coordinates=[ (float(random.randint(-900,900))/10.0,float(random.randint(0,3599))/10.0) for i in range(100)]
        for set_of_sample_coordinates in sample_coordinates:
            self.assertEqual(interpret("%f,%f" % set_of_sample_coordinates),coordinates(set_of_sample_coordinates[0],set_of_sample_coordinates[1]))
        
        for coordinates_set in VALID_COORDINATE_SAMPLES:
            #import pdb; pdb.set_trace()
            self.assertEqual(interpret(coordinates_set[0]),coordinates(coordinates_set[1][0],coordinates_set[1][1]))
    
    def test_interpret_angle(self):
        self.assertEqual(interpret_angle(u"49.234°"),latitude(49.234))
        self.assertEqual(interpret_angle(u"49.234° 0.00'"),latitude(49.234))
        self.assertEqual(interpret_angle(u"49.234° 24.2' 14\""),latitude(49.641222222222225))
    
    def test_coordinates(self):
        self.assertEqual(coordinates(1,2),coordinates(1,2.0))

if __name__ == '__main__':
    unittest.main()
