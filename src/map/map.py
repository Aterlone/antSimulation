from map.tiles import tile, dirt, empty

class Map:
    def __init__(self, startSize):
        self.size = startSize
        self.map = []

    def createMap(self, queen):
        type = empty.Empty

        for i in range(self.size[0]): 
            line = []
            for j in range(self.size[1]):
                if ((i > queen.pos[1] - 10 and i < queen.pos[1] + queen.size[1] + 10) and (j > queen.pos[0] - 10 and j < queen.pos[0] + queen.size[0] + 10)):
                    type = empty.Empty
                else:
                    type = dirt.Dirt
                line.append(type([j,i]))
            self.map.append(line)
    
    def __str__(self):
        mapStr = ""
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                mapStr += f"{self.map[i][j].type.value} "
            mapStr += "\n"
        return mapStr