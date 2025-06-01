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

def fill_group(y, x, region_map):

    region_map[y][x] = str(groups)

    if y and region_map[y-1][x] == '#':

        region_map = fill_group(y-1, x, region_map)
    
    if x and region_map[y][x-1] == '#':

        region_map = fill_group(y, x-1, region_map)
    
    if y < len(region_map) - 1 and region_map[y+1][x] == '#':
        
        region_map = fill_group(y+1, x, region_map)
    
    if x < len(region_map) - 1 and region_map[y][x+1] == '#':

        region_map = fill_group(y, x+1, region_map)
    
    return region_map

drive = []

for row in range(128):

    my_hash = knot_hash(f'{key}-{row}')
    #print(my_hash)
    drive.append(list(''.join(bin(int(i, 16))[2:].zfill(4) for i in my_hash).replace('1', '#').replace('0', '.')))

region_map = drive.copy()
groups = 0

for y in range(len(drive)):
    
    for x in range(len(drive[y])):

        if region_map[y][x] == '#':

            groups += 1

            region_map = fill_group(y, x, region_map)


print(region_map)
print(groups)