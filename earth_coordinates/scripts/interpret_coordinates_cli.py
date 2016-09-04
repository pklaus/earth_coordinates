#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philippklaus.de

from earth_coordinates import Coordinates, Latitude, Longitude
from earth_coordinates import CoordinateInterpretationError, interpret, interpret_angle

def main():
    try:
        while True:
            try:
                inp = raw_input("Enter Coordinates: ")
            except:
                inp = input("Enter Coordinates: ")
            try:
                coordinates = interpret(inp)
            except CoordinateInterpretationError:
                print("Sorry, I could not interpret your input.")
                continue
            print(coordinates)
    except (EOFError, KeyboardInterrupt):
        #print("\n[Ctrl]-[c] pressed. Exiting...")
        print("")
        pass

if __name__ == '__main__':
    main()
