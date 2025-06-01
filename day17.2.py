from structlinks.DataStructures import LinkedList

with open('day17.txt') as f:
    step = int(f.read().strip())

#spin = LinkedList([0])
cur_pos = 0

after_num = None
after_len = 0

for i in range(1, 50_000_000): #50_000_001

    cur_pos = ((cur_pos + step) % i) + 1

    if cur_pos == 1:

        after_num = i
        after_len += 1
        #print("after 0", "num =", i, "aft-len =", after_len, "cur-pos =", cur_pos)
    
    else:

        after_len += 1

print(after_num)
