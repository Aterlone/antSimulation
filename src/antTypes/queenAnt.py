from antTypes import ant, workerAnt

import random as r

class QueenAnt(ant.Ant):
    def __init__(self, vel, size):
        super().__init__(vel, size)
        self.pos = [45, 30]
        self.maxHidration = 80
        self.hidration = 80

        self.turns = 10

    def spawn(self):
        if self.turns > 15:
            self.turns = 0
            return [workerAnt.WorkerAnt([r.randint(-1, 1), r.randint(-1, 1)], [1, 1], self.pos) for i in range(5)]
        
        self.turns += 1