""" This program will calculate exponontials of base and exponention input by user."""
base = int(input("Enter the value of base.-> "))
power = int(input("Enter the value of exponention.-> "))
ANSWER =1

for i in range (1,power+1):
    ANSWER *=base
print(str(base)+" to the power "+str(power)+" = "+str(ANSWER))
