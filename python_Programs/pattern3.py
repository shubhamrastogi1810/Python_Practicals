# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
"""  printing the above pattern """

last = int(input("Enter the no. of rows "))
OUT = 1

while OUT<=last:
    INN = 1
    while INN <= OUT:
        print(OUT," ",end='')
        INN+=1
    print()
    OUT+=1
