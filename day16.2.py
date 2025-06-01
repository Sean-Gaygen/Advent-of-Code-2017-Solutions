with open('day16.txt') as f:
    dance = f.read().split(',')

line = list('abcdefghijklmnop')

#The only thing the changes our algorithm is the name swapping one, crunch those parts down
cycle = 0


def run_dance(line, dance):

    for move in dance:

        match move[0]:

            case 's':

                movers = line[-int(move[1:]):]
                line = movers + line[:-int(move[1:])]

            case 'x':

                a, b = move[1:].split('/')

                hold = line[int(a)]
                line[int(a)] = line[int(b)]
                line[int(b)] = hold
            
            case 'p':

                a, b = move[1:].split('/')

                line_str = ''.join(line)

                a_pos = line_str.find(a)
                b_pos = line_str.find(b)

                hold = line[a_pos]
                line[a_pos] = b
                line[b_pos] = hold
    
    return line


for i in range(1_000_000_000):

    line = run_dance(line, dance)
    
    if line == list('abcdefghijklmnop'):

        cycle = i + 1 
        break

line = list('abcdefghijklmnop')

for _ in range(1_000_000_000 % cycle):

    line = run_dance(line, dance)

print(''.join(line))