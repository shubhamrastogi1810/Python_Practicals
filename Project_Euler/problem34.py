import math
add = 0

def curious(num):
    summ = 0
    while num > 0:
        temp = num % 10
        summ += math.factorial(temp)
        num = num // 10
    return summ	

for i in range(3,9999999):
    if i == curious(i):
        add+=i
print(add)
