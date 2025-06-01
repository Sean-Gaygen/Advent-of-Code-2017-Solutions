import itertools as it

with open('day24.txt') as f:
    mags = [(int(i.strip().split('/')[0]), int(i.strip().split('/')[1])) for i in f.readlines()]

valid_bridges = set()

def build_bridges(bridge):

    valid_bridges.add(tuple(bridge))

    hold = bridge.copy()
    hold2 = bridge.copy()
    num = bridge[-1][1]

    for mag in mags:

        if mag not in bridge and mag[::-1] not in bridge:

            if num == mag[0]:
                #print('num 0;', num, bridge[-1], mag)
                hold.append(mag)
                build_bridges(hold)
                hold = bridge.copy()

            if num == mag[1] and mag[0] != mag[1]:
                #print('num 1;', num, mag[::-1], bridge[-1])
                hold2.append(mag[::-1])
                build_bridges(hold2)
                hold2 = bridge.copy()

for start in filter(lambda x: 0 in x, mags):

    build_bridges([start])

tot = 0
max_len = 0
long_bridges = []

for bridge in valid_bridges:

    max_len = max(max_len, len(bridge))

for bridge in valid_bridges:

    if len(bridge) == max_len:

        long_bridges.append(bridge)


for bridge in long_bridges:
    #print(bridge)
    
    mini_tot = 0

    for blah in bridge:

        mini_tot += sum(blah)
    
    tot = max(tot, mini_tot)

#print(valid_bridges)
print(tot)

