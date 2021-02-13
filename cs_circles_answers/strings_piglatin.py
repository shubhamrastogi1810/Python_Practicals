"""This program inputs a word and translates it into pig latin language."""
#For example, monkey becomes onkeymay in Pig Latin, and word becomes ordway.
inp_str = input()
newinp = inp_str[1:]
newstr = newinp + inp_str[0] + 'ay'
print(newstr)
