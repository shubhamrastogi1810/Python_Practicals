# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
""" printing the above pattern """

last = int(input("Enter the no. of rows "))
A = 1
F =1
while A<=last:
    B = 1
    while B<=A:
        print(F," ",end='')
        F+=1
        B+=1
    print()
    A+=1
