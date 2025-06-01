with open('day20.txt') as f:
    raw_particles = [i.strip() for i in f.readlines()]

class Particle:

    all_particles = []
    max_pos = float('-inf')
    min_pos = float('inf')

    def build_particles(raw_data):

        for name, par in enumerate(raw_data):
        
            pos, vel, acc = par[:-1].split('>, ')

            pos = [int(i) for i in pos[3:].split(',')]
            vel = [int(i) for i in vel[3:].split(',')]
            acc = [int(i) for i in acc[3:].split(',')]

            Particle.max_pos = max(Particle.max_pos, max(pos + vel + acc))
            Particle.min_pos = min(Particle.min_pos, min(pos + vel + acc))
            Particle.all_particles.append(Particle((name, pos, vel, acc)))
        
        print(f"Max position = {Particle.max_pos}. Min position = {Particle.min_pos}")
    
    def run():

        for _ in range(Particle.max_pos + abs(Particle.min_pos)):

            if not _ % 100:

                print(_)

            for par in Particle.all_particles:

                par.move()
            
            for par in Particle.all_particles:

                if par.active:

                    par.collision_check()


    def __init__(self, data):

        self.name = data[0]
        self.pos = data[1]
        self.vel = data[2]
        self.acc = data[3]
        self.active = 1
    
    def move(self):

        pos_x, pos_y, pos_z = self.pos
        vel_x, vel_y, vel_z = self.vel
        acc_x, acc_y, acc_z = self.acc

        self.vel = (vel_x + acc_x, vel_y + acc_y, vel_z + acc_z)
        self.pos = (pos_x + (vel_x + acc_x), pos_y + (vel_y + acc_y), pos_z + (vel_z + acc_z))
    
    def collision_check(self):

        for par_ind in range(Particle.all_particles.index(self), len(Particle.all_particles)):

            par = Particle.all_particles[par_ind]

            if par.active and par != self and par.pos == self.pos:

                print('run')

                par.active = 0
                self.active = 0

if __name__ == '__main__':

    Particle.build_particles(raw_particles)
    Particle.run()
    print(len([i for i in Particle.all_particles if i.active]))
