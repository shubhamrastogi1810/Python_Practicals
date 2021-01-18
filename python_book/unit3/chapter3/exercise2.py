""" This program will determine that the number inputed is even or not using function."""
def determine_number(number):
    """ functioin will determine that a number inputed is even or odd."""
    if number % 2 == 0:
        print(number," is even.")
    else:
        print(number," is odd.")

numb = int(input("Enter number-> "))
determine_number(numb)
