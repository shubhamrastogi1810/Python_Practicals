""" This is a lab exercise of python book example 10."""
import random
def roll_dice(num_rolls,sides=6):
    """ This function prints the sides on rolling, then prints 'that's all.'  """
    number = 0
    while number < num_rolls:
        print(random.randrange(1,sides))
        number+=1


number_roll = int(input("Enter the num of rolls.->"))
roll_dice(number_roll)
print("That's all!\n")
roll_dice(number_roll)
print("That's all!\n")
