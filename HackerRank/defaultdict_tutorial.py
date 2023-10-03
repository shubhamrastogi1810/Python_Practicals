"""
Input Format

The first line contains integers,n and m separated by a space.
The next lines contains the words belonging to group A.
The next lines contains the words belonging to group B.

Constraints
1 <= n <= 10000
1 <= m <= 100
1 <= length of each word in the input <= 100


Output Format

Output m lines.
The ith line should contain the 1 -indexed positions of the occurrences of the ith word separated by spaces.

Sample Input

STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b

Sample Output

1 2 4
3 5

Explanation

'a' appeared 3 times in positions 1,2 and 4.
'b' appeared 2 times in positions 3 and 5.
In the sample problem, if 'c' also appeared in word group B, you would print -1.
"""
from collections import defaultdict

d = defaultdict(list)
x,y = list(map(int,input().strip().split(' ')))
val = []
for i in range(x):
	val.append(input().strip())
for i in range(y):
	char = input().strip()
	index = []
	flag = 0
	for a in range(len(val)):
		if val[a] == char:
			index.append(a+1)
			flag = 1
	if flag == 1:
		for i in index:
			print(i,end=' ')

	else:
		print('-1',end=' ')
	print()
		
	
