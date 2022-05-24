l = [1, 2, 3, 4, 5, 2, 3, 4, 7, 9, 5]
l1 = []
for i in l:
	if i not in l1:
		l1.append(i)
	else:
		print(i, end=' ')

from collections import Counter


def do_find_duplicates(x):
	x = input("Enter a word = ")
	for key, val in Counter(x).items():
		print(key, val)
