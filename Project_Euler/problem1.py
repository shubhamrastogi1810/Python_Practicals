""" this program will print the sum of multiples of 3 or 5 below 1000."""
ADD = 0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        ADD+=i
print(ADD)
