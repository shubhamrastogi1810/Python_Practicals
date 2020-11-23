""" This will print the pattern given below """
#111
#11
#1
value=int(input())
while value >= 1:
    for i in range(0,value):
        print(1,end='')
    print()
    value-=1
