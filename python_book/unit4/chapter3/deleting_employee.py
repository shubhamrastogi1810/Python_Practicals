"""This program inputs record(name & phonenumber) from file, and deletes the input name record"""
# Write a program to create a phone book and delete particular phone number using name.
FRMT = '{:10} : {:}'
phonebook = {}
total_numbers = int(input("Enter total number of records to enter. "))
filevar = open('phonebook_read.txt','r')
for i in range(total_numbers):
    name,number = filevar.readline().split(',')
    phonebook[name] = number
filevar.close()
print("\n\tPhone Book")
for i in phonebook:
    print(FRMT.format(i,phonebook[i]))
record_delete = input("Enter record name you want to delete. ")

if record_delete in phonebook:
    del phonebook[record_delete]
    for key in phonebook:
        print(FRMT.format(key,phonebook[key]))
else:
    print("Record doesn't exist. ")
