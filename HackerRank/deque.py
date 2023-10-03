"""
Task

Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format

The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.

Constraints

0 < N < 100

Output Format

Print the space separated elements of deque d.

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output

1 2

"""
from collections import deque
d = deque()
for i in range(int(input())):
	a = input().split()
	if a[0] == "append":
		d.append(int(a[-1]))
	elif a[0] == "appendleft":
		d.appendleft(int(a[-1]))
	elif a[0] == "pop":
		d.pop()
	elif a[0] == "popleft":
		d.popleft()
print(' '.join(list(map(str,list(d)))))
