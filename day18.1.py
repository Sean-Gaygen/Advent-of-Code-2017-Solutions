with open('day18.txt') as f:
    instructions = [i.strip().split(' ') for i in f.readlines()]

registers = {}
last_played_sound_freq = 0

for register in set([i[1] for i in instructions]):

    registers[register] = 0

index = 0

while index < len(instructions):

    op = instructions[index][0]
    reg_a = instructions[index][1]
    reg_b = None

    if len(instructions[index]) > 2:

        hold = instructions[index][2] 
        reg_b = int(hold) if hold[-1].isnumeric() else registers[hold]
    


    match op:

        case 'snd':

            last_played_sound_freq = registers[reg_a]

        case 'set':

            registers[reg_a] = reg_b

        case 'add':

            registers[reg_a] += reg_b

        case 'mul':

            registers[reg_a] *= reg_b

        case 'mod':

            registers[reg_a] %= reg_b

        case 'rcv':

            if last_played_sound_freq:
                
                print(last_played_sound_freq)
                break

        case 'jgz':

            if registers[reg_a] > 0:

                index += reg_b - 1
    
    index += 1