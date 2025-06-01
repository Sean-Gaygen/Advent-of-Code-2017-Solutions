import re

with open('day2.txt') as f:
	data_hold = [re.sub('\s+', ' ', i).strip().split(' ') for i in f.readlines()]
	data = [list(map(int, i)) for i in data_hold]

tot = 0

for line in data:
	
	for num in line:
		
		for check_num in line:
			
			if num != check_num and num % check_num == 0:
				print(num)
				tot += max(num, check_num) // min(num, check_num)

print(tot)