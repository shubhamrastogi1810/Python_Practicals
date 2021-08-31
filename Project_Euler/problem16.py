"""
    This code will do summation of answer of individual numbers of a number raised to power.
"""
NUM = 2 ** 1000
SUMS = 0
while NUM > 0:
    TEMP = NUM % 10
    SUMS +=TEMP
    NUM//=10
print(SUMS)
