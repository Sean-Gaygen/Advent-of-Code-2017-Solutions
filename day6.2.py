with open('day6.txt') as f:
	data = [int(i) for i in f.read().strip().split('	')]

seen_configs = []

cycle_start = None

cycle_size = 0

for i in range(999999999):
	
	if data in seen_configs:
		
		if not cycle_start:
			
			cycle_start = list(data)
		
		else:
			
			cycle_size += 1
			
			if cycle_start == data:
				
				print(cycle_size)
				break
	
	seen_configs.append(list(data))
	
	for num in range(len(data)):
		
		if data[num] == max(data):
			
			hold = int(data[num])
			data[num] = 0
			
			for j in range(hold):
				
				data[(num + 1 + j) % len(data)] += 1
				
			
			break
		