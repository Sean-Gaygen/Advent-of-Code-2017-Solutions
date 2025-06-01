with open('day19.txt') as f:
    maze = [list(i.replace('\n', '')) for i in f.readlines()]  # We stop at Y because I got lucky and saw it.

y = 0
x = maze[0].index('|')

up = 0
right = 1
down = 2
left = 3

direction = down
letters = ''


def move(y, x, direction):

    if direction == up:

        return (y-1, x)

    elif direction == down:

        return (y+1, x)
    
    elif direction == right:

        return (y, x+1)
    
    elif direction == left:

        return (y, x-1)
    
    else:

        raise ValueError

steps = 0

while 1:
    
    steps += 1
    if maze[y][x] == 'Y':

        letters += maze[y][x]
        break

    elif maze[y][x].isalpha():

        letters += maze[y][x]

    elif maze[y][x] == '+':

        if direction == up or direction == down:

            direction = right if maze[y][x+1] == '-' or maze[y][x+1].isalpha() else left
        
        else:

            direction = up if maze[y-1][x] == '|' or maze[y-1][x].isalpha() else down
        
    y, x = move(y, x, direction)

print(steps)