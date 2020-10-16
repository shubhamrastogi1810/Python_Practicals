# Establish a dictionary which translates 'cat', 'dog', and 'mouse' into French.
en_to_fr = { 'cat':'chat', 'dog':'chein','mouse':'souris' }

# Add 'snake' to it.
en_to_fr['snake'] = 'serpant'

# Print the dictionary
print(en_to_fr,"\n\n")

print(en_to_fr.keys(),"\n")

print(en_to_fr.values(),"\n")

print(en_to_fr.items(),"\n")

for (english,spanish) in en_to_fr.items():
	print(spanish,english)
	print("\n")

print(list(en_to_fr.items()))

print('snake' in en_to_fr)




