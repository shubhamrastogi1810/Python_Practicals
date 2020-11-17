""" prime numbers print in the given range """
for i in range(1,1000,2):
    f=0
    for j in range(2,i):
        if f == 1:
            break
        else:
            if i%j==0:
                f=1
if f == 0:
    print(i)
