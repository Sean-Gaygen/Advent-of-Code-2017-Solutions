with open('day3.txt') as f:
	target = int(f.read())

for i in range(1,9999, 2):
	
	if i**2 >= target:
		
		if i**2 == target:
			print(i + 1)
			break
		
		middle = (i // 2) + 1
		
		edge = i**2
		
		blah = min(abs(target - (edge - (middle - 1))),
			abs(target - ((edge - (i * 2) + 2) + (middle - 1))),
			abs(target - ((edge - (i * 3) + 3) + (middle - 1))),
			abs(target - ((edge - (i * 3) + 3) - (middle - 1))))
		
		print([abs(target - (edge - (middle - 1))),
			abs(target - ((edge - (i * 2) + 2) + (middle - 1))),
			abs(target - ((edge - (i * 3) + 3) + (middle - 1))),
			abs(target - ((edge - (i * 3) + 3) - (middle - 1)))])
		
		print([((edge - (middle - 1))),
			((edge - (i * 2) + 2) + (middle - 1)),
			((edge - (i * 3) + 3) + (middle - 1)),
			((edge - (i * 3) + 3) - (middle - 1))])
		
		print(blah)
		print(middle)
		print(edge, i)
		
		print(blah + middle - 1) # answer
		break