"""This code will input 2 set of values for 2 tuples and will swap it."""
val1 = int(input("Enter the values to be entered in tuple1"))
tup1 = tuple()
for i in range(val1):
    tup1+=(input(),)
val2 = int(input("Enter the values to be entered in tuple2"))
tup2 = tuple()
for i in range(val2):
    tup2+=(input(),)

print("Before Swap")
print("Tup1 ",tup1)
print("Tup2 ",tup2)

tup1,tup2 = tup2,tup1
print("After Swap")
print("Tup1 ",tup1)
print("Tup2 ",tup2)
