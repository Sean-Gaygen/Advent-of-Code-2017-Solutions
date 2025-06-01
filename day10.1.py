with open('day10.txt') as f:
    lengths = [int(i) for i in f.read().strip().split(',')]

knot = list(range(256))

cur_pos = 0
skip = 0

for length in lengths:

    list_segment = []
 
    for i in range(length):

        list_segment.append(knot[(cur_pos + i) % len(knot)])
    
    list_segment.reverse()

    for i in range(len(list_segment)):

        knot[(cur_pos + i) % len(knot)] = list_segment[i]
    
    cur_pos += (length + skip) % len(knot)
    skip += 1

print(knot[0] * knot[1])
