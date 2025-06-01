with open('day12.txt') as f:
    pipes = [i.strip() for i in f.readlines()]


class Pipe:

    all_pipes = {}

    groups = []

    grouped_numbers = set()

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

for cur_pipe in Pipe.all_pipes:

    if Pipe.all_pipes[cur_pipe].name not in Pipe.grouped_numbers:

        Pipe.all_pipes[cur_pipe].check_conn()

        Pipe.grouped_numbers.update(Pipe.tmp_visited_nodes)
        Pipe.groups.append(Pipe.tmp_visited_nodes)
        Pipe.tmp_visited_nodes = set()

print(len(Pipe.groups))