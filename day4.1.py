with open('day4.txt') as f:
	data = [i.strip().split(' ') for i in f.readlines()]

tot = 0

for i in data:
	
	tot += 1 if len(i) == len(set(i)) else 0
	
print(tot)