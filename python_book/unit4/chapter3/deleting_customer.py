""" This program will input record from a file and will delete the record of the name entered."""
customers = {}
FRMT = '{:9}:{:}'
total_customer = int(input("Enter total number of customers.-> "))
filevar = open('phonebook_read.txt','r')
for i in range(total_customer):
    name,number = filevar.readline().split(',')
    customers[name] = number
filevar.close()
print("\n\t Customers Detail.\n")
for i in customers:
    print(FRMT.format(i,customers[i]))
delete_name = input("Enter the name you want to delete.-> ")

if delete_name in customers:
    del customers[delete_name]
    print("\n\t Record Deleted.\n")
    for i in customers:
        print(FRMT.format(i,customers[i]))
else:
    print("Record does not exist.")
