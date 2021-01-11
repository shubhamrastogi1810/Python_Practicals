""" This is an example of python book of exercise Example5. """
# This example will input a number and returns TRUE is no. is odd else FALSE without
# using if.
def finding_odd(number):
    """ This function will return boolean if no. is odd."""
    return bool(number%2)
print(finding_odd(int(input("Enter a number-> "))))
