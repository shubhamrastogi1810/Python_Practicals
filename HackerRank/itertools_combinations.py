"""
Task

You are given a string S..
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Input Format
A single line containing the string S and integer value k separated by a space.

Constraints

0 < k <= len(S)
The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string S on separate lines.

SAMPLE INPUT

HACK 2

SAMPLE OUTPUT

A
C
H
K
AC
AH
AK
CH
CK
HK  
"""
from itertools import combinations

a,b = input().split(' ')
a = list(a)
a.sort()
for i in range(1,int(b)+1 ):
	ass = list(combinations(a,i))
	for k in ass:
		print(''.join(k))

