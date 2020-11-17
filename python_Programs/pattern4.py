# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
"""  printing the above pattern """

last = int(input("Enter the no. of rows "))
A = 1#out loop variable
# B is inner loop variable
while A<=last:
    B = A
    while A>=1:
        print(B," ",end='')
        B-=1
    print()
    A+=1
