""" This program will input a name and will print a song on it's name."""
#our program will take a person's name as input, for example "pearl," and print song

# pearl, pearl, bo-bearl
# banana-fana fo-fearl
# fee-fi-mo-mearl
# pearl!

inp_str = input()
first = inp_str + ', ' + inp_str + ', '+ 'bo-b'+inp_str[1:]
second = 'banana-fana fo-f' + inp_str[1:]
third  = 'fee-fi-mo-m' + inp_str[1:]
fourth = inp_str + '!'
print(first)
print(second)
print(third)
print(fourth)
