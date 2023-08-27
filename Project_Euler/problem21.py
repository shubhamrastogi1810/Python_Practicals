check_numbers = []

def factor(a):
    factors = []
    for i in range(1,a//2+1):
        if a % i == 0:
            factors.append(i)
    return sum(factors)
    
for num in range(1,10001):    
    if num in check_numbers:
        continue
    else:
        ans = factor(num)
        temp = factor(ans)
        if num == temp and ans == factor(temp):
            if num != factor(num):
                check_numbers.append(num)
                check_numbers.append(ans)
print(sum(check_numbers))
