#find the list for even and odd numbers
start = int(input("Enter a start number "))
length = int(input("Enter the length of list "))

for a in range(0,length):
	if start % 2:
		print (start," even ")
	else:
		print (start," odd ")
	start+=1

