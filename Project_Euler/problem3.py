"""
    This code will find the largest prime factor for the following number.
"""
NUM = 600851475143
def isprime(num):
    """
        This function will return bool value if input number is prime or not.
    """
    flag = True
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            flag = False
            break
    return bool(flag)

FACTORS = []
for temp in range(3,int(NUM**0.5)+1):
    if NUM % temp == 0:
        FACTORS.append(temp)
FACTORS.reverse()
for j in FACTORS:
    if isprime(j):
        print(j)
        break
