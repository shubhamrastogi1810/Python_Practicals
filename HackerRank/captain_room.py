from collections import Counter

num = int(input())
a = dict(Counter(map(int,input().split(' '))))
for k,v in a.items():
	if v == 1:
		print(k)
