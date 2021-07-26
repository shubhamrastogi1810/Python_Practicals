""" This program will print Weird/Not Weird based on the conditions stated below."""
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

number = int(input())
if number % 2 != 0:
    print("Weird")
else:
    if number in range(2,6):
        print("Not Weird")
    elif number in range(6,21):
        print("Weird")
    elif number > 20:
        print("Not Weird")
