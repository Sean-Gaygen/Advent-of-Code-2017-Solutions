import re

with open('day2.txt') as f:
	data_hold = [re.sub('\s+', ' ', i).strip().split(' ') for i in f.readlines()]
	data = [list(map(int, i)) for i in data_hold]

print(sum([abs(max(i) - min(i)) for i in data])) 