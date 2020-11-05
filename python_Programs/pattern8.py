# 1
# 0 0
# 1 1 1
# 0 0 0 0 
# 1 1 1 1 1
no = int(input("Enter number of rows "))
a = 1 
while a <= no:
	b=1
	while b<=a:
		if a % 2 == 0:
			print("0 ",end='')
		else:
			print("1 ",end='')
		b+=1
	print()	
	a+=1

