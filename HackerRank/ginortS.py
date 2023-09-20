"""
You are given a string S.
contains alphanumeric characters only.
Your task is to sort the string ginortS in the following manner:

    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.

Input Format

A single line of input contains the string S.

Constraints

0 < len(S) < 1000

Output Format

Output the sorted string S.

Sample Input

Sorting1234

Sample Output

ginortS1324
"""

string = input()

upper = []
lower = []
even = []
odd = []
for i in string:
    if i.isalpha():
        if i.isupper():
            upper.append(i)
        if i.islower():
            lower.append(i)
    if i.isdigit():
        if int(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
upper.sort()
lower.sort()
even.sort()
odd.sort()
print(''.join(lower+upper+odd+even))
