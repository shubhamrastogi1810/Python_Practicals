# this is reading the file content using for loop

book = open("abc.txt","r")

for  line in book:
	print(line)

book.close()
