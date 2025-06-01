import queue

with open('day9.txt') as f:
    stream = f.read().strip()

clean_string = ''
is_in_garbage = 0

index = 0

while index < len(stream):

    cur_char = stream[index]

    if cur_char == '<':
    
        is_in_garbage = 1
    
    elif cur_char == '!':

        index += 1
    
    elif cur_char == '>' and is_in_garbage:

        is_in_garbage = 0
    
    elif not is_in_garbage:

        clean_string += cur_char

    index += 1

tot = 0

brackets = queue.LifoQueue()

for char in clean_string:

    if char == '{':

        brackets.put(char)
    
    if char == '}':

        tot += brackets.qsize()
        brackets.get()

print(tot)