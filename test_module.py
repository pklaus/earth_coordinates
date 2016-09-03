#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philippklaus.de

import unittest
import random
import re

from earth_coordinates import interpret, interpret_angle, CoordinateInterpretationError
from earth_coordinates import Coordinates, Latitude
from earth_coordinates.interpret import DEG_MIN_SEC_ANGLE

VALID_COORDINATE_SAMPLES = ( (  "20.123 N, 19.132 E", ( 20.123, 19.132)  )  ,
                             (  "20.123, 19.132",     ( 20.123, 19.132)  )  ,
                             (  "N20.123, E19.132",   ( 20.123, 19.132)  )  ,
                             (  u'49.234° 24.2\' 14 N, 49.234° 24.2\' 14" E ',   ( 49.641222222222225, 49.641222222222225)  )  ,
                           )

class test_module(unittest.TestCase):

    def test_interpret(self):
        self.assertEqual(interpret("11,10"), Coordinates(11, 10))

    def test_interpret_random(self):
        sample_coordinates=[ (float(random.randint(-900, 900))/10.0, float(random.randint(0, 3599))/10.0) for i in range(100)]
        for set_of_sample_coordinates in sample_coordinates:
            self.assertEqual(interpret("%f,%f" % set_of_sample_coordinates), Coordinates(set_of_sample_coordinates[0], set_of_sample_coordinates[1]))

    def test_interpret_valid(self):
        for coordinates_set in VALID_COORDINATE_SAMPLES:
            try:
                with self.subTest(coordinates_set=coordinates_set):
                    try:
                        self.assertEqual(interpret(coordinates_set[0]), Coordinates(coordinates_set[1][0], coordinates_set[1][1]))
                    except CoordinateInterpretationError:
                        self.fail("Raised CoordinateInterpretationError for test set {}".format(coordinates_set))
            except AttributeError:
                """ .subTest() exists since Python 3.4 """
                try:
                    self.assertEqual(interpret(coordinates_set[0]), Coordinates(coordinates_set[1][0], coordinates_set[1][1]))
                except CoordinateInterpretationError:
                    self.fail("Raised CoordinateInterpretationError for test set {}".format(coordinates_set))

    def test_interpret_angle(self):
        self.assertEqual(interpret_angle("49.234°"), Latitude(49.234))
        self.assertEqual(interpret_angle("49.234° 0.00'"), Latitude(49.234))
        self.assertEqual(interpret_angle("49.234° 24.2' 14\""), Latitude(49.641222222222225))

    def test_coordinates(self):
        self.assertEqual(Coordinates(1, 2), Coordinates(1, 2.0))

if __name__ == '__main__':
    unittest.main()
