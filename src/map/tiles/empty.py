from map.tiles import tile

class Empty(tile.Tile):
    def __init__(self, pos):
        super().__init__(pos)

    def moisture(self):
        return 0
    
    def color(self):
        return ""
    
    def speedMult(self):
        return 1