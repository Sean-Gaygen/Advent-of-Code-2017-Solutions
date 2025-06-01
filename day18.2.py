import time
import multiprocessing

with open('day18.txt') as f:
    instructions = [i.strip().split(' ') for i in f.readlines()]


class Duet:

    def __init__(self, id, sfb, a_wait, b_wait, a_q, b_q):

        self.id = id
        self.registers = {}
        self.last_played_sound_freq = 0
        self.stuck = 0
        self.a_waiting = a_wait
        self.b_waiting = b_wait
        self.sent_from_b = sfb
        self.a_queue = a_q
        self.b_queue = b_q

        for register in set([i[1] for i in instructions]):

            if not register.isnumeric():

                self.registers[register] = self.id if register == 'p' else 0

    def run(self):

        index = 0

        while index < len(instructions) and not self.stuck:

            print(self.id, index, self.a_waiting.value, self.b_waiting.value)
            op = instructions[index][0]
            reg_a = instructions[index][1]
            reg_b = None

            if len(instructions[index]) > 2:

                hold = instructions[index][2] 
                reg_b = int(hold) if hold[-1].isnumeric() else self.registers[hold]
            
            match op:

                case 'snd':

                    #print(self.id, 'sent', int(reg_a) if reg_a.isnumeric() else self.registers[reg_a], '\n', reg_a)

                    if self.id == 0:

                        self.b_queue.put(int(reg_a) if reg_a.isnumeric() else self.registers[reg_a])
                    
                    else:

                        self.sent_from_b.value += 1
                        self.a_queue.put(int(reg_a) if reg_a.isnumeric() else self.registers[reg_a])

                case 'set':

                    self.registers[reg_a] = reg_b

                case 'add':

                    self.registers[reg_a] += reg_b

                case 'mul':

                    self.registers[reg_a] *= reg_b

                case 'mod':

                    self.registers[reg_a] %= reg_b

                case 'rcv':
                    
                    if self.id == 0:

                        if self.a_queue.empty():

                            self.a_waiting.value = 1

                            while self.a_queue.empty():

                                print(" a wait", self.a_waiting.value, self.b_waiting.value, self.stuck)

                                if self.a_waiting.value and self.b_waiting.value and self.a_queue.empty() and self.b_queue.empty():
                                    
                                    self.stuck = 1
                                    break
                                
                                time.sleep(0.1)
                                
                        if not self.stuck:

                            self.a_waiting.value = 0
                            self.registers[reg_a] = self.a_queue.get()
                    
                    else:

                        if self.b_queue.empty():

                            self.b_waiting.value = 1

                            while self.b_queue.empty():

                                print("b wait", self.a_waiting.value, self.b_waiting.value, self.stuck)

                                if self.a_waiting.value and self.b_waiting.value and self.a_queue.empty() and self.b_queue.empty():
                                    
                                    self.stuck = 1
                                    break
                                    
                                time.sleep(0.1)

                        if not self.stuck:
                            
                            self.b_waiting.value = 0
                            self.registers[reg_a] = self.b_queue.get()
                                
                case 'jgz':

                    comp = int(reg_a) if reg_a.isnumeric() else self.registers[reg_a]

                    if comp > 0:

                        index += reg_b - 1
    
            index += 1
        
        print(self.id, "Done", self.registers)
        
        if self.id == 0:
            
            self.a_waiting.value = 1
        
        else: 

            self.b_waiting.value = 1


if __name__ == '__main__':

    a_waiting = multiprocessing.Value('i', 0)
    b_waiting = multiprocessing.Value('i', 0)
    a_queue = multiprocessing.Queue()
    b_queue = multiprocessing.Queue()
    sent_from_b = multiprocessing.Value('i', 0)

    a = Duet(0, sent_from_b, a_waiting, b_waiting, a_queue, b_queue)
    b = Duet(1, sent_from_b, a_waiting, b_waiting, a_queue, b_queue)

    p1 = multiprocessing.Process(target=a.run)
    p2 = multiprocessing.Process(target=b.run)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(b.sent_from_b.value)