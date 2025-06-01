with open('day20.txt') as f:
    raw_particles = [i.strip() for i in f.readlines()]

particles = []

for name, par in enumerate(raw_particles):
    
    pos, vel, acc = par[:-1].split('>, ')

    pos = [int(i) for i in pos[3:].split(',')]
    vel = [int(i) for i in vel[3:].split(',')]
    acc = [int(i) for i in acc[3:].split(',')]

    particles.append((name, pos, vel, acc))

min_particle = None
min_particle_num = 999999999999999999

for i in particles:

    name, pos, vel, acc = i

    if sum([abs(i) for i in acc]) < min_particle_num:

        min_particle_num = sum([abs(i) for i in acc])
        min_particle = i
    
print(min_particle)