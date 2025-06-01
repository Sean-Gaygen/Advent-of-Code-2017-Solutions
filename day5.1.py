with open('day5.txt') as f:
	data = [int(i) for i in f.readlines()]

"""def jump(index, steps):
	
	#print(index, steps)
	
	if index >= len(data):
		return steps
	
	steps += 1
	data[index] += 1
	index += data[index] - 1
	return jump(index, steps)

print(jump(0, 0))"""  # This should have worked :^(. Recursion limits eh...

index = 0

for i in range(9999999999):
	
	#print(data)
	
	if index >= len(data):
		print(i)
		break
	
	hold = int(data[index])
	data[index] += 1 if data[index] < 3 else -1
	index += hold
	