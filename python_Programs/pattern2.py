# * * * * *
# * * * *
# * * * 
# * * 
# *  
# printing the above pattern

last = int(input("Enter the no. of rows "))
a = last 

while a>=1:
	b = 1
	while b<=a:
		print(" *",end='')
		b+=1
	print()
	a-=1

