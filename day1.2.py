with open('day1.txt') as f:
	data = f.read().strip()

list_len = len(data)

tot = 0

for next_num, num in enumerate(data, list_len // 2):
	
	if next_num != len(data) and num == data[next_num % list_len] or \
		next_num == len(data) and num == data[0]:
		
		tot += int(num)
	
print(tot)