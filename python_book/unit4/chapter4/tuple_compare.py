"""This code will input 2 value sets for 2 tuples and will print th result"""
# eg. t1 = (10,20,30)
# t2 = (10)
# output:-  cmp => 1
val1 = int(input("Enter the value for tuple1 "))
tup1 = tuple()
tup2 = tuple()
for i in range(val1):
    tup1+=(input(),)
val2 = int(input("Enter the value for tuple2 "))
for i in range(val2):
    tup2+=(input(),)

if len(tup1) == len(tup2):
    print("cmp:- 0")
elif len(tup1) > len(tup2):
    print("cmp:- 1")
else:
    print("cmp:- -1")
