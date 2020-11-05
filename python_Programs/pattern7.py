# 1
# 2 3 
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# printing the above pattern

last = int(input("Enter the no. of rows "))
a = 1
f =1
while a<=last:
	b = 1
	while b<=a:
		print(f," ",end='')
		f+=1
		b+=1
	print()
	a+=1

