#print fibonacci series in this pattern 1,1,2,3,5,8,13,21.......
length = int(input("enter the digits to print "))
f = 1 # first term
l = 0 # second term
a = 0
summ = 0
while a < length:
	summ = f + l
	print(summ," ",end='')
	f = l
	l = summ
	a+=1
print()	
