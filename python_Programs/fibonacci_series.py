""" print fibonacci series in this pattern 1,1,2,3,5,8,13,21....... """
length = int(input("enter the digits to print "))
F = 1# first term
L = 0# second term
A = 0
SUMM = 0
while A < length:
    SUMM = F + L
    print(SUMM," ",end='')
    F = L
    L = SUMM
    A+=1
print()
