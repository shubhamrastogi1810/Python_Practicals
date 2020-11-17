# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
"""  printing the above pattern """

last = int(input("Enter the no. of rows "))
A = last

while A>=1:
    B = 1
    while B<=A:
        print(A," ",end='')
        B+=1
    print()
    A-=1
