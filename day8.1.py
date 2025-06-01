with open('day8.txt') as f:
    instructions = [i.strip() for i in f.readlines()]

registers = {}

for instruction in instructions:

    op, cond = instruction.split(' if ')

    op_register, operation, amount = op.split(' ')
    cond_register = cond.split(' ')[0]

    if op_register not in registers.keys():

        registers[op_register] = 0
    
    if cond_register not in registers.keys():

        registers[cond_register] = 0
    
    if eval(f'{registers[cond_register]} {" ".join(cond.split()[1:])}'):

        registers[op_register] += int(amount) if operation == "inc" else -int(amount)

print(max(registers.values()))