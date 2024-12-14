class Ant:
    def __init__(self, vel, size):
        self.maxHidration = 40
        self.hidration = 40
        self.vel = vel
        self.pos = [10,10]
        self.size = size

    def dehidrate(self):
        self.hidration -= 1
        if self.hidration == 0:
            return 1
        return 0