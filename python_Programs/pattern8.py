# 1
# 0 0
# 1 1 1
# 0 0 0 0
# 1 1 1 1 1
""" printing the above pattern """
no = int(input("Enter number of rows "))
A = 1
while A <= no:
    B = 1
    while B <= A :
        if A % 2 == 0:
            print("0 ",end='')
        else:
            print("1 ",end='')
        B+=1
    print()
    A+=1
