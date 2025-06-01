with open('day15.txt') as f:
    init_a, init_b = f.read().split(' ')

print(init_a, init_b)

def generator_a(start):

    val_hold = int(start)

    while 1:

        new_num = (val_hold * 16807) % 2147483647
        #print(new_num, val_hold)
        yield bin(new_num)[2:]

        val_hold = new_num
        
def generator_b(start):

    val_hold = int(start)

    while 1:

        new_num = (val_hold * 48271) % 2147483647
        #print(new_num)
        yield bin(new_num)[2:]

        val_hold = new_num

    
tot = 0

gen_a = generator_a(init_a)
gen_b = generator_b(init_b)

for i in range(40_000_000):

    bin_a = next(gen_a)
    bin_b = next(gen_b)

    bin_a = bin_a.zfill(max(len(bin_a), len(bin_b)))
    bin_b = bin_b.zfill(max(len(bin_a), len(bin_b)))


    # print(bin_a)
    # print(bin_b)

    # print(bin_a[-16:] == bin_b[-16:])

    tot += 1 if bin_a[-16:] == bin_b[-16:] else 0

print(tot)
