import itertools as it

with open('day4.txt') as f:
	data_hold = [i.strip().split(' ') for i in f.readlines()]
	
	data = []
	
	for line in data_hold:
		
		line_hold = []
		
		for word in line:
			
			line_hold.append(''.join(sorted(word)))
		
		data.append(line_hold)
	
tot = 0

for i in data:
	
	tot += 1 if len(i) == len(set(i)) else 0
	
print(tot)