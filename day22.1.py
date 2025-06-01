with open('day22.txt') as f:
    grid = [i.strip() for i in f.readlines()]

class Sporifica:

    def __init__(self, raw_grid):

        self.grid = {}
        self.y = len(raw_grid) // 2
        self.x = len(raw_grid) // 2
        print(self.x, self.y)
        self.direction = 0
        self.infected_tally = 0

        for y in range(len(raw_grid)):

            for x in range(len(raw_grid[y])):

                self.grid[f'{str(y)}+{str(x)}'] = 1 if raw_grid[y][x] == '#' else 0
    
    def __repr__(self):

        max_x = -float('inf')
        max_y = -float('inf')
        min_x = float('inf')
        min_y = float('inf')

        for node in self.grid:

            y, x = [int(i) for i in node.split('+')]

            max_x = max(max_x, x)
            min_x = min(min_x, x)
            max_y = max(max_y, y)
            min_y = min(min_y, y)
        
        #print(max_x, max_y, min_x, min_y)
        #print(self.grid)
        
        ret_list = [['.'] * (max_x + abs(min_x) + 1) for _ in range(max_y + abs(min_y) + 1)]

        for node in self.grid:

            if self.grid[node]:

                y, x = [int(i) for i in node.split('+')]
                ret_list[y + abs(min_y)][x + abs(min_x)] = '#'
        
        return '\n'.join([''.join(line) for line in ret_list]) + '\n'
            


    def move(self):

        pos_str = f'{str(self.y)}+{str(self.x)}'

        if pos_str not in self.grid.keys():

            self.grid[pos_str] = 0
        
        self.direction += 1 if self.grid[pos_str] else -1
        self.direction %= 4

        self.infected_tally += 0 if self.grid[pos_str] else 1
        self.grid[pos_str] = 0 if self.grid[pos_str] else 1

        match self.direction:
            
            case 0:  # up

                self.y -= 1
            
            case 1:  # right

                self.x += 1
            
            case 2:  # down

                self.y += 1

            case 3:  # left

                self.x -= 1

if __name__ == '__main__':

    x = Sporifica(grid)

    for _ in range(10000):

        print(x)
        x.move()
    
    print(x.infected_tally)