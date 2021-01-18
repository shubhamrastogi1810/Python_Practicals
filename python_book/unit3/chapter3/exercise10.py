""" This program imports random module and stimulares tossing a coin n times."""
import random

toss_time = int(input("Enter the number of cossing a coin.-> "))
for i in range(0,toss_time):
    number = random.randint(0,1)
    if number == 0:
        print("Tails")
    elif number == 1:
        print("Heads")
