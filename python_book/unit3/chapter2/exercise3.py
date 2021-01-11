""" This is lab exercise of python book Example 3. """
# Write a script that asks a user for a number. Then adds 3 to that number, and then
# multiplies the result by 2, subtracts twice the original number, then prints the
# result.

def compute_result(number):
    """ This function wil add 3 to no. then doubles it, subtract 2x and print result"""
    new_number = number + 3
    new_number *= 2
    new_number -= 2*number
    print(new_number)

compute_result(int(input("Enter a integer Number-> ")))
