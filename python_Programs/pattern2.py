# * * * * *
# * * * *
# * * *
# * *
# *
"""  printing the above pattern """

last = int(input("Enter the no. of rows "))
A = last

while A>=1:
    B = 1
    while B<=A:
        print(" *",end='')
        B+=1
    print()
    A-=1
