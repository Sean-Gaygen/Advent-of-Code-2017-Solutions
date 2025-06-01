with open('day17.txt') as f:
    step = int(f.read())

spin = [0]
cur_pos = 0

for i in range(1, 2018):

    cur_pos = ((cur_pos + step) % i) + 1

    spin.insert(cur_pos, i)


print(spin[cur_pos + 1])