"""This program counts number of times of string1 occuring in string2."""
#for example "assesses" has the substring "sses" 2 times, and
#"trans-Panamanian banana" has the substring "an" 6 times.

string1 = input()#substring
string2 = input()#mainstring
COUNT = 0
for i in range(0,len(string2)):
    if string1 == string2[i:(i+len(string1))]:
        COUNT+=1
print(COUNT)
