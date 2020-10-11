book = open("abc.txt","r")
n_word = 0

for line in book:
	word_in =len(line.split())
	n_word += word_in
	
print("No of words",n_word)
book.close()
