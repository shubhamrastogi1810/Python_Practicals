"""This code will input values for tuple and will slice it into 2 tuples for odd value and even."""
number =int(input("Enter the number you want to enter."))
t = tuple()

for i in range(number):
    t+=(int(input()),)
t1 = t[::2]
t2 = t[1::2]
print(t1,t2)
