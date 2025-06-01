with open('day3.txt') as f:
	target = int(f.read())

spiral = {'00': 1,
	'01': 1}

current_pos = (1, 1)

def dir_check():
	
	current_total = 0
	
	y, x = current_pos
	
	left = str(x - 1)
	right = str(x + 1)
	up = str(y + 1)
	down = str(y - 1)

	valid_numbers = spiral.keys()
	
	if up + left in valid_numbers:
		current_total += spiral[up + left]
	
	if up + str(x) in valid_numbers:
		current_total += spiral[up + str(x)]
	
	if up + right in valid_numbers:
		current_total += spiral[up + right]
	
	if str(y) + left in valid_numbers:
		current_total += spiral[str(y) + left]
	
	if str(y) + right in valid_numbers:
		current_total += spiral[str(y) + right]
	
	if down + left in valid_numbers:
		current_total += spiral[down + left]
	
	if down + str(x) in valid_numbers:
		current_total += spiral[down + str(x)]
	
	if down + right in valid_numbers:
		current_total += spiral[down + right]
	
	return current_total

for i in range(99999999999):
	
	y, x = current_pos
	filled_nums = spiral.keys()
	current_num = dir_check()
	
	#print(current_num)
	
	if current_num > target:
		print(current_num)
		break
	
	up = str(y + 1) + str(x)
	down = str(y - 1) + str(x)
	left = str(y) + str(x - 1)
	right = str(y) + str(x + 1)
	
	spiral[str(y) + str(x)] = current_num
	
	if down in filled_nums and not left in filled_nums:
		current_pos = (y, x - 1)
	
	elif right in filled_nums and not down in filled_nums:
		current_pos = (y - 1, x)
	
	elif up in filled_nums and not right in filled_nums:
		current_pos = (y, x + 1)
	
	elif left in filled_nums and not up in filled_nums:
		current_pos = (y + 1, x)
	
	