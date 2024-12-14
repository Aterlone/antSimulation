from antTypes import ant
from map.tiles import dirt, empty

import random as r

class WorkerAnt(ant.Ant):  
    def __init__(self, vel, size, queenPos):
        super().__init__(vel, size)
        self.pos = [pos + r.randint(0,5) for pos in queenPos]
        self.maxHidration = 40
        self.hidration = 40
        self.stored = 5
        
        self.path = []
        
        self.timeTillBirth = 5
        
    def move(self, targetTile):
        amount = targetTile.moisture()

        def needWater():
            if self.hidration > self.maxHidration*3/4:
                self.hidration += amount
            else:
                self.stored += amount

        if not self.timeTillBirth:
            #chemicals layed to get back to the queen
            self.path.append(self.pos)
    
            self.pos = [self.pos[i] + self.vel[i] * targetTile.speedMult() for i in range(2)]
            
            if amount:
                needWater()
                return 1
            else:
                return 0
            
        self.timeTillBirth -= 1