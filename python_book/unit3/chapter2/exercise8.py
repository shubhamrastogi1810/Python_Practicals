""" This program will input a number and computes log, sine, square, and cosine for that number."""
import math
FRMT = '{:15}:{:}'
def computation(number):
    """ This function will compute log, square,sin, and cos of a number."""
    print(FRMT.format("Logarithm",math.log(number)))
    print(FRMT.format("Square",number*number))
    print(FRMT.format("Sin",math.sin(number)))
    print(FRMT.format("Cosine",math.cos(number)))

computation(int(input("Enter a Number-> ")))
