"""This code will input data from a txt file and print contact no. if that data is in dictionary"""

# This  program to input'n' names and phone numbers to store it in dictionary
# from phonebook_read.txt and will print the phone number of the person if found
# in the dictionary.
FRMT = '{:10} :  {:}'
total_names = int(input("Enter the total number of names for input. "))
phonebook = {}
file_read = open("phonebook_read.txt","r")
for i in range(total_names):
    name,number = file_read.readline().split(',')
    phonebook[name] = number.strip()
file_read.close()
print("Phonebook Directory\n")
print(FRMT.format("Name","Number"),"\n")
item = phonebook.items()
for key,val in item:
    print(FRMT.format(key,val))

search_name = input("Enter the name to search in phonebook ")
if search_name in phonebook:
    print(phonebook.get(search_name))
else:
    print("Record does not exist.")
