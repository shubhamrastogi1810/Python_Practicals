""" This program will perform the following arithmatic operation and prints the result. """
# Write a script that asks a user for a number. Then adds 3 to that number, and   then
# multiplies the result by 2, subtracts twice the original number, then prints    the result.

def compute_result(number):
    """ This function is performing x+3, 2x,X -2x and print a static value 6."""
    new_number = number + 3
    new_number *= 2
    new_number -= 2*number
    print(new_number)

compute_result(int(input("Enter a integer Number-> ")))
