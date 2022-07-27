#The first two consecutive numbers to have two distinct prime factors are:

#14 = 2 × 7
#15 = 3 × 5

#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.

#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?


def check_prime(num):
    if num == 2:
        return True
    flag = 0
    if num % 2 == 0:
        return False
    else:
        flag = 0
        for i in range(3,num//2 + 1,2):
            if num % i == 0:
                flag = 1 
                break
        if flag == 1:
            return False
        else:
            return True

def finding_factors(num):
    factors = []
    if num % 2 == 1:
        for i in range(3,num//2+1,2):
            if num % i == 0:
                factors.append(i)
    else:
        for i in range(2,num//2 + 1):
            if num % i == 0:
                factors.append(i)
    x = []
    for i in factors:
        if check_prime(i):
            x.append(i)
    if len(x) == 4:
        return True
    else:
        return False


# initializing from 10K as already checked for values below 10K.
first = 10000
second = 10001
third = 10002
while True:
    i = third + 1 
    if ((finding_factors(first) and finding_factors(second)) and finding_factors(third)) and finding_factors(i):
        print(first)
        break
    first = second
    second = third
    third = i


