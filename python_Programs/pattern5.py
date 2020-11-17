# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
""" printing the above pattern """

last = int(input("Enter the no. of rows "))
A = 1

while A<=last:
    B = 1
    while B<=A:
        print(A," ",end='')
        B+=1
    print()
    A+=1
