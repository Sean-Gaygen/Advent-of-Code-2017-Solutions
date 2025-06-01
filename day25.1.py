line = {}
pos = 0
state = 'A'

for _ in range(12964419): # run for x steps

    if pos not in line.keys():

        line[pos] = 0

    z = line[pos] == 0 # z for zero state

    match state:

        case 'A':

            line[pos] = 1 if z else 0
            pos += 1
            state = 'B' if z else 'F'

        case 'B':
            
            line[pos] = 0 if z else 1
            pos += -1
            state = 'B' if z else 'C'
        
        case 'C':

            line[pos] = 1 if z else 0
            pos += -1 if z else 1
            state = 'D' if z else 'C'

        case 'D':

            line[pos] = 1
            pos += -1 if z else 1
            state = 'E' if z else 'A'
        
        case 'E':

            line[pos] = 1 if z else 0
            pos += -1
            state = 'F' if z else 'D'

        case 'F':

            line[pos] = 1 if z else 0
            pos += 1 if z else -1
            state = 'A' if z else 'E'


print(sum(line.values()))