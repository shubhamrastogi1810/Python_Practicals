"""This program will repeatedlyinput a number until an even is entered and prints message acc."""
while True:
    number = int(input("Enter a number-> "))
    if number % 2 == 1:
        print("please re-enter the number as the previous number was odd.")
        number = int(input("Enter a number-> "))
    else:
        break
print("Congratulations! Even number entered.")
