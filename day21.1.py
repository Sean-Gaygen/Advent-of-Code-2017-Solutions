import numpy as np

with open('day21.txt') as f:
    enhancement = [i.strip() for i in f.readlines()]

class Art:


    def __init__(self, enh: list):

        self.art =[['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]
        self.patterns = {}

        for rule in enh:

            pattern, output = rule.split(' => ')
            output = [list(i) for i in output.split('/')]
            
            self.patterns[pattern] = output
    
    def format(string):

        return '\n'.join([''.join(i) for i in string])
    
    def get_shapes(self, chunk: list):

        ninety = [list(x) for x in np.rot90(chunk)]
        one_eighty = [list(x) for x in np.rot90(ninety)]
        seven_twenty = [list(x) for x in np.rot90(one_eighty)]

        rev_x = chunk[::-1]
        rev_x_90 = [list(x) for x in np.rot90(rev_x)]
        rev_x_180 = [list(x) for x in np.rot90(rev_x_90)]
        rev_x_270 = [list(x) for x in np.rot90(rev_x_180)]

        rev_y = [list(x) for x in np.fliplr(chunk)]
        rev_y_90 = [list(x) for x in np.rot90(rev_y)]
        rev_y_180 = [list(x) for x in np.rot90(rev_y_90)]
        rev_y_270 = [list(x) for x in np.rot90(rev_y_180)]
#         print(f"""chunk = \n{Art.format(chunk)},
# 90 = \n{Art.format(ninety)},
# 180 = \n{Art.format(one_eighty)},
# 270 = \n{Art.format(seven_twenty)},
# reversed = \n{Art.format(rev_x)},
# rev 90 = \n{Art.format(rev_x_90)},
# rev 180 = \n{Art.format(rev_x_180)},
# rev 270 = \n{Art.format(rev_x_270)}
# y = \n{Art.format(rev_y)}
# y 90 = \n{Art.format(rev_y_90)}
# y 180 = \n{Art.format(rev_y_180)}
# y 270 = \n{Art.format(rev_y_270)}\n\n""")

        return [chunk, ninety, one_eighty, seven_twenty, rev_x, rev_x_90, rev_x_180, rev_x_270, rev_y, rev_y_90, rev_y_180, rev_y_270]

    def stringify(self, chunk: list):
        #print('in,', chunk)
        #print('out', '/'.join([''.join(x) for x in chunk]))
        return '/'.join([''.join(x) for x in chunk])

    def chunk_art(self, n: int):

        ret_chunks = [[0] * (len(self.art) // n) for _ in range(len(self.art) // n)]
        #ret_chunks = [[] for _ in range(len(self.art) // n)]
        #print('in chunk', ret_chunks, self.art)
        #print(n, ret_chunks, (len(self.art) // n), len(self.art), self.art)
        y_index = 0
        x_index = 0

        #print('input = ', self.art)

        """for _ in range((len(self.art) // n) ** 2):
        
            chunk = []

            for y_offset in range(n):

                x_line = []

                for x_offset in range(n):
                    #print(self.art, y_index, y_offset, x_index, x_offset)
                    x_line.append(self.art[y_index + y_offset][x_index + x_offset])
                
                #chunk.append(x_line)

                ret_chunks[y_index // n][x_index // n] = chunk
            ret_chunks[y_index // n] = chunk

            if x_index + n >= len(self.art):

                x_index = 0
                y_index += n
            
            else:

                x_index += n"""
        #print('len', (len(self.art) // n) ** 2, len(self.art[0]))
        for chunk_index in range(((len(self.art) // n)) ** 2):

            chunk = []

            for y_offset in range(n):

                line = []

                for x_offset in range(n):

                    line.extend(self.art[y_index + y_offset][x_index + x_offset])
                
                chunk.append(line)

            if x_index + n >= len(self.art[0]):
                x_index = 0
                y_index += n
            
            else:
                x_index += n

            #print(ret_chunks, 'n', n,'art len', len(self.art),'index', chunk_index, 'index / n', chunk_index // n, chunk)
            ret_chunks[chunk_index // len(ret_chunks)][chunk_index % len(ret_chunks)] = chunk


        #print('return = ', ret_chunks)
        return ret_chunks

    def dechunk(self, art): # TODO reversing x atm

        #print('in', art)
        ret_list = []

        """for y in range(len(art)):

            line = []

            for x in range(len(art)):

                #print(art)
                line += art[y][x]
            
            ret_list.append(line)"""
        #print('1', len(art) * len(art[0][0]), len(art), len(art[0][0]))
        for y in range(len(art) * len(art[0][0])):
            #print('y', y)
            line = []

            for x in range(len(art[0])):
                #print('gack',y, len(art[0][0]), y // len(art[0][0]))
                line += (art[(y // len(art[0][0]))][x][y % len(art[0][0])])
                #print('line', line)
                #print(f'indexes;\n1 = {y // len(art[0][0])},\n2 = {x},\n3 = {y % len(art[0][0])}\ny = {y}, len art[0][0] = {len(art[0][0])}' )
            
            ret_list.append(line)

        #print('ret', ret_list)
        return ret_list
    
    def run(self, cycles: int):

        for _ in range(cycles):
            #print(self.art)

            chunked_art = self.chunk_art(2) if not len(self.art) % 2 else self.chunk_art(3)
            #print('here', chunked_art)
            #new_art = [[] * (len(chunked_art) if len(chunked_art) else 1) for _ in range(len(chunked_art) if len(chunked_art) else 1)]
            new_art = [[] for _ in range(len(chunked_art))]
            #print(new_art)

            for y in range(len(chunked_art)):

                for x in range(len(chunked_art)):

                    shape_strings = [self.stringify(shape) for shape in self.get_shapes(chunked_art[y][x])]
                    #print(shape_strings, self.patterns.keys())
                    for key in self.patterns.keys():

                        if key in shape_strings:
                            #print(y, x)
                            #new_art[y][x] = self.patterns[key]
                            #print(key, shape_strings, self.patterns[key])
                            new_art[y].append(self.patterns[key])
                            break
            #print('here', new_art)
            self.art = self.dechunk(new_art)
            print(_)
            #print('\n'.join([''.join(i) for i in self.art]))
            print()
    
if __name__ == '__main__':

    x = Art(enhancement)
    x.run(5)

    print(sum([''.join(i).count('#') for i in x.art]))
    #print('\n'.join([''.join(i) for i in x.art]))
#132 & 133 & 134 too low