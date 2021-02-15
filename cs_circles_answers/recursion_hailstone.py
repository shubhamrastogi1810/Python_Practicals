""" This program will print hailstone series using recursive function hailstone(n)"""
# hailstone sequence is that if the entered number n is even then next number would
# be n/2 or if its odd then next number will be 3*n+1.
def hailstone(number):
    """ This recursive function will print hailstone series from number n."""
    if number == 1:
        print(1)
    else:
        print(int(number))
        if number % 2 == 0:
            hailstone(number/2)
        else:
            hailstone(3*number+1)
value = int(input("Enter a number to print hailstone series. "))
hailstone(value)
