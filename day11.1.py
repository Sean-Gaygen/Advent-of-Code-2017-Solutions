with open('day11.txt') as f:
    directions = f.read().strip() + ','

dir_hold = directions.replace('n,', '', directions.count('s,')).replace('s,', '', directions.count('n,'))
dir_hold_2 = dir_hold.replace('ne,', '', dir_hold.count('sw,')).replace('sw,', '', dir_hold.count('ne,'))
dir_hold_3 = dir_hold_2.replace('nw,', '', dir_hold_2.count('se,')).replace('se,', '', dir_hold_2.count('nw,'))
dir_hold_4 = None
dir_hold_5 = None
dir_hold_6 = None

if dir_hold_3.count('ne,') > dir_hold_3.count('nw,'):
    
    dir_hold_4 = dir_hold_3.replace('ne,', 'n,', dir_hold_3.count('nw,')).replace('nw,', '')

else:

    dir_hold_4 = dir_hold_3.replace('nw,', 'n,', dir_hold_3.count('ne,')).replace('ne,', '')


if dir_hold_4.count('se,') > dir_hold_4.count('sw,'):
    
    dir_hold_5 = dir_hold_4.replace('se,', 's,', dir_hold_4.count('sw,')).replace('sw,', '')

else:

    dir_hold_5 = dir_hold_4.replace('sw,', 's,', dir_hold_4.count('se,')).replace('se,', '')


if dir_hold_5.count('s,') and dir_hold_5.count('ne,'):

    dir_hold_6 = dir_hold_5.replace('ne,', 'se,', dir_hold_5.count('s,')).replace('s,', '')

elif dir_hold_5.count('se,'):

    dir_hold_6 = dir_hold_5.replace('se,', 'ne,', dir_hold_5.count('n,')).replace('n,', '')

else:

    dir_hold_6 = dir_hold_5

print(len(dir_hold_6.split(',')) - 1, sorted(dir_hold_6.split(',')))
# print()
# print(dir_hold)
# print(dir_hold_2)
# print(dir_hold_3)
# print(dir_hold_4)
# print(dir_hold_5)
# print(dir_hold_6)