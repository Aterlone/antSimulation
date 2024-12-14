from map.tiles import tile

class Dirt(tile.Tile):
    def __init__(self, pos):
        super().__init__(pos)

    def moisture(self):
        return 1
    
    def color(self):
        return "orange"
    
    def speedMult(self):
        return -1