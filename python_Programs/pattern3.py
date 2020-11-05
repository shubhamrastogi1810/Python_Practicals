# 1
# 1 2 
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# printing the above pattern

last = int(input("Enter the no. of rows "))
a = 1

while a<=last:
	b = 1
	while b<=a:
		print(a," ",end='')
		b+=1
	print()
	a+=1

