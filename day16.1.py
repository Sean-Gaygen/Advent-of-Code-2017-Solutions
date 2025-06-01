with open('day16.txt') as f:
    dance = f.read().split(',')

line = list('abcdefghijklmnop')


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

print(''.join(line))