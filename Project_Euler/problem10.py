"""
    This code will print the summation of prime numbers below 2 million.
"""
SUMS = 2
for i in range(3,2000000,2):
    FLAG = False
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            FLAG = True
            break
    if FLAG is False:
        SUMS+=i
print(SUMS)
