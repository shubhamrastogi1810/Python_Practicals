""" This program will input a number and returns True if number is odd else False."""
# This example will input a number and returns TRUE if number is odd else
# returns False without using if.
def finding_odd(number):
    """ This function will return True if no. is odd. without using if."""
    return bool(number%2)
print(finding_odd(int(input("Enter a number-> "))))
