"""
    this program calculates the 10001th prime number.
"""
lis = [2,3]
NUM = 5
while len(lis) != 10001:
    FLAG = True
    for j in range(2,int(NUM**0.5)+1):
        if NUM % j == 0:
            FLAG = False
            break
    if FLAG is True:
        lis.append(NUM)
    NUM+=2
print(lis[-1])
