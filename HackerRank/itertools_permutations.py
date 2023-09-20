"""
Task

You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string Sand the integer value k.

Constraints

0 < k <= len(S)
The string contains only UPPERCASE characters.

Output Format

Print the permutations of the string S on separate lines.

Sample Input

HACK 2

Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

"""

from itertools import permutations

a,b = input().split(' ')

a = list(a)
a.sort()
per = permutations(a,int(b))
for i in per:
	print(''.join(i))
