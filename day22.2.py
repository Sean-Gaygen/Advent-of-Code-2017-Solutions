import time

with open('day22.txt') as f:
    grid = [i.strip() for i in f.readlines()]

class Sporifica:

    def __init__(self, raw_grid):

        self.grid = {}
        self.y = len(raw_grid) // 2
        self.x = len(raw_grid) // 2
        #print(self.x, self.y)
        self.direction = 0
        self.infected_tally = 0

        for y in range(len(raw_grid)):

            for x in range(len(raw_grid[y])):

                self.grid[f'{str(y)}+{str(x)}'] = 2 if raw_grid[y][x] == '#' else 0
    
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

            y_hold, x_hold = [int(i) for i in node.split('+')]

            y = y_hold + abs(min_y)
            x = x_hold + abs(min_x)

            if self.grid[node] == 1:

                ret_list[y][x] = 'W'

            elif self.grid[node] == 2:

                ret_list[y][x] = '#'
            
            elif self.grid[node] == 3:

                ret_list[y][x] = 'F'
        
        return '\n'.join([' '.join(line) for line in ret_list]) + '\n'

    def move(self):

        pos_str = f'{str(self.y)}+{str(self.x)}'

        if pos_str not in self.grid.keys():

            self.grid[pos_str] = 0
        
        match self.grid[pos_str]:

            case 0:  # clean

                self.direction = (self.direction - 1) % 4

            case 1:  # weakened

                self.direction += 0

            case 2:  # infected

                self.direction = (self.direction + 1) % 4
            
            case 3:  # flagged

                self.direction = (self.direction + 2) % 4

        self.grid[pos_str] = (self.grid[pos_str] + 1) % 4
        self.infected_tally += 1 if self.grid[pos_str] == 2 else 0

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

    for _ in range(10000000):

        #print(x)
        x.move()
        #time.sleep(0.1)
    
    print(x.infected_tally)

# 2511944 too high