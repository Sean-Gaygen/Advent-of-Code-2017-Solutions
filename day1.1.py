with open('day1.txt') as f:
	data = f.read().strip()

tot = 0

for next_num, num in enumerate(data, 1):
	
	if next_num != len(data) and num == data[next_num] or \
		next_num == len(data) and num == data[0]:
		
		tot += int(num)
	
print(tot)