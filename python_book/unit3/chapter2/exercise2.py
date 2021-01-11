""" This program will rectify the errors, which occurs in the comment code. """
# Consider the following function definition:
# def intDiv(x,a):
# """
# x : a non-negative integer argument
# a : a positive integer argument
# returns : integer, the integer division of x divided by a.
# """
# while x>=a:
# count +=1
# x = x-a
# return count
# when we call
# print intDiv(5,3)
# We get an error message. Modify the code so that error does not occur.
def intdiv(dividend,divisor):
    """
    x: a non-negative integer arugment
    a: a positive integer argument
    returns integer, the integer division of x divided by a.
    """
    count = 0
    while dividend>=divisor:
        count +=1
        dividend = dividend-divisor
    return count
print(intdiv(12,3))
