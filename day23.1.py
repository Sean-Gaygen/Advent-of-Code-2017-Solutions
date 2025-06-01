with open('day23.txt') as f:
    instructions = [i.strip().split(' ') for i in f.readlines()]

registers = {}
mul_tot = 0

for register in 'abcdefgh':

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

        case 'set':

            registers[reg_a] = reg_b

        case 'sub':

            registers[reg_a] -= reg_b

        case 'mul':

            registers[reg_a] *= reg_b
            mul_tot += 1

        case 'jnz':

            cond = registers[reg_a] if reg_a.isalpha() else int(reg_a)

            if cond != 0:

                index += reg_b - 1
    
    index += 1

print(mul_tot)