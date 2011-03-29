#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philippklaus.de

import unittest
import random

import re
from interpret import DEG_MIN_SEC_ANGLE

from interpret import interpret, interpret_angle
from coords import coords

VALID_COORDINATE_SAMPLES = ( (  "20.123 N, 19.132 S", (20.123,  19.132)  )  ,
                             (  "20.123, 19.132",     (20.123,  19.132)  )  ,
                           )

class test_coordinates(unittest.TestCase):

    def test_interpret(self):
        self.assertEqual(interpret("11,10"),coords(11,10))
        
        sample_coords=[ (float(random.randint(0,360)),float(random.randint(0,360))) for i in range(100)]
        for set_of_sample_coords in sample_coords:
            self.assertEqual(interpret("%d,%d" % set_of_sample_coords),coords(set_of_sample_coords[0],set_of_sample_coords[1]))
        
        for coords_set in VALID_COORDINATE_SAMPLES:
            self.assertEqual(interpret(coords_set[0]),coords(coords_set[1][0],coords_set[1][1]))
    
    def test_interpret_angle(self):
       self.assertEqual(interpret_angle(u"49.234°"),49.234)
       self.assertEqual(interpret_angle(u"49.234° 0.00'"),49.234)
       self.assertEqual(interpret_angle(u"49.234° 24.2' 14\""),49.641222222222225)

if __name__ == '__main__':
    unittest.main()
