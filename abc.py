# read all the file content without loop

book = open("abc.txt","r")
line=book.read()
print(line)
book.close()
