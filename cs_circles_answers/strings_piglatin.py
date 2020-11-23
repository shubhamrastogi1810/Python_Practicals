""" input a string and translates it form english to pig latin """
#For example, monkey becomes onkeymay in Pig Latin, and word becomes ordway.
# Write a program that takes a single word as input and translates it to Pig Latin.
inp_str = input()
newinp = inp_str[1:]
newstr = newinp + inp_str[0] + 'ay'
print(newstr)
