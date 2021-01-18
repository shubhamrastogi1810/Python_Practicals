""" This program will print a countdown to 0 from a number inputed."""
number = int(input("enter a number-> "))
print()
if number > 0:
    while number >= 0:
        print(number)
        number-=1
else:
    print("Invalid Input")
