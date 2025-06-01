with open('day14.txt') as f:
    key = f.read().strip()

def knot_hash(key):
    
    knot = list(range(256))
    worked_key = [int(i) for i in (','.join([str(ord(i)) for i in key]) + ',17,31,73,47,23').split(',')]

    cur_pos = 0
    skip = 0

    for _ in range(64):

        for length in worked_key:

            list_segment = []
        
            for i in range(length):

                list_segment.append(knot[(cur_pos + i) % len(knot)])
            
            list_segment.reverse()

            for i in range(len(list_segment)):

                knot[(cur_pos + i) % len(knot)] = list_segment[i]
            
            cur_pos += (length + skip) % len(knot)
            skip += 1

    dense_hash = []

    for group in range(0, 255, 16):

        result = knot[group]

        for number in knot[group + 1: group + 16]:

            result ^= number

        dense_hash.append(result)

    output = ''

    for i in dense_hash:

        hold = hex(i)[2:]

        if len(hold) == 1:

            hold = '0' + hold
        
        output += hold
    
    return output

drive = []

for row in range(128):

    my_hash = knot_hash(f'{key}-{row}')
    #print(my_hash)
    drive.append(''.join(bin(int(i, 16))[2:].zfill(4) for i in my_hash))

print(sum([i.count('1') for i in drive]))