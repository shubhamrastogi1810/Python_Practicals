#!/usr/bin/python3
""" Find the square root of a number """
import math
FRMT = '{:.2f}'
a = abs(int(input("Enter a number ")))
print("square root is ",FRMT.format(math.sqrt(a)))
