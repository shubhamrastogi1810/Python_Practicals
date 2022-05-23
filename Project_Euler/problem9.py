# problem 9 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# finding the product of that triplet.

n = 1000

flag = False
for i in range(100,n//3,2):
    for j in range(101,n//2,2):
        k = n - i - j 
        if i*i + j*j == k * k:
            print(i,j,k)
            flag = True
            break
    if flag:
        break
print('The product of {:3d} {:3d} {:3d} is {:d} '.format(i,j,k,i*j*k))
