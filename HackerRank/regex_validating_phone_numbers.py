"""
Concept

A valid mobile number is a ten digit number starting with a 7,8 or 9.

Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.

https://developers.google.com/edu/python/regular-expressions

Input Format

The first line contains an integer N, the number of inputs.

N lines follow, each containing some string.

Constraints

1 <= N <= 10
2 <= len(number) <= 15

Output Format

For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

Sample Input

2
9587456281
1252478965

Sample Output

YES
NO
"""
import re

pattern = r'^[7-9]\d{9}$'
val = int(input())
for i in range(val):
    string = input()
    match = re.match(pattern,string)
    if match:
        print('YES')
    else:
        print('NO') 
