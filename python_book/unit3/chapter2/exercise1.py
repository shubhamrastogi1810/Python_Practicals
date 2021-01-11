""" This program will input first-name, last-name, and date-of-birth and prints them in a format."""
# Write a program to ask for follwing as input
# Enter your first name: Rahul
# Enter your last name: Kumar
# Enter your date of birth Month? March Day? 10 Year? 1992 and display on the screen.
from datetime import date
FRMT = '{:20}:{}'
def getdata():
    """ This function is to get fname, lname and date of birth and prints them."""
    fname = input("Enter your First Name-> ")
    lname = input("Enter your Last Name-> ")
    bir_month = int(input("Birth Month in Number-> "))
    bir_day = int(input("Birth Day-> "))
    bir_year = int(input("Birth year-> "))
    birthdate = date(bir_year,bir_month,bir_day)
    print(FRMT.format('First Name',fname))
    print(FRMT.format('Last Name',lname))
    print(FRMT.format('Birthday',birthdate.strftime("%d/%B/%y")))

getdata()
