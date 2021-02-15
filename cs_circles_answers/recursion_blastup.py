"""This program prints Blastoff! followed by numbers from 1 to n using a recursive function"""
def countup(number):
    """ This is a recursive function to print numbers from 1 to n and print Blastoff at last."""
    if number == 0:
        print('Blastoff!')
    else:
        countup(number - 1)
        print(number)
countup(10)
