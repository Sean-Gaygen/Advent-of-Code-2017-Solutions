with open('day12.txt') as f:
    pipes = [i.strip() for i in f.readlines()]


class Pipe:

    all_pipes = {}

    tmp_visited_nodes = set()

    def make_pipes():

        for pipe in pipes:

            Pipe(pipe)

    def check_conn(self):

        Pipe.tmp_visited_nodes.add(self.name)

        for i in self.conn:

            if i not in Pipe.tmp_visited_nodes:
                
                Pipe.all_pipes[i].check_conn()


    def __init__(self, line):

        self.name, hold = line.split(' <-> ')
        self.conn = hold.split(', ')
        Pipe.all_pipes[self.name] = self
    
        
    
Pipe.make_pipes()

Pipe.all_pipes['0'].check_conn()

print(len(Pipe.tmp_visited_nodes))