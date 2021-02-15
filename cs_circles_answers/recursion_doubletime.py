"""This program uses a recursive function to count down  increment by 2."""
def countdownby2(number):
    """ THis recursive function will count down the increment by 2 and then prints Blastoff!"""
    if number <= 0:
        print('Blastoff!')
    else:
        print(number)
        countdownby2(number - 2)
countdownby2(5)
