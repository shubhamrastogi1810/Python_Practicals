""" This program computes 10 lakh numbers for Prime/Composite and stores it in a boolean list."""

isprime = [True] * 22

def checkprime(number):
    """This function will check that a number is prime or not, returns bool value accordingly."""
    if number in (2,3):
        return True
    if number % 2 == 0 or number < 2:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

for count in range(0, len(isprime)):
    isprime[count] = checkprime(count)

print(isprime)
