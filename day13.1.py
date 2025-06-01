with open('day13.txt') as f:
    layers_hold = [i.strip() for i in f.readlines()]

layers = {}
tot = 0

for layer in layers_hold:

    name, depth = layer.split(': ')

    layers[name] = int(depth)

for picosecond in range(max([int(i) for i in layers.keys()]) + 1):

    if str(picosecond) in layers.keys():

        cycle = (layers[str(picosecond)] - 1) * 2

        if not picosecond % cycle:

            tot += picosecond * layers[str(picosecond)]

print(tot)