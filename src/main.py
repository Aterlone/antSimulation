import tkinter as tk
import time
import pyautogui

from antTypes import queenAnt
from map import map, camera
from map.tiles import dirt, empty

class Game:
    def __init__(self):
        self.queens = [queenAnt.QueenAnt([0,0], [5, 5])]
        self.workers = []

        self.worldMap = map.Map([100,100])
        self.worldMap.createMap(self.queens[0])

        # playerCam = camera.Camera([250, 250])

        self.dim = [750, 750]
        self.root = tk.Tk()
        self.root.title("Ant Simulation")
        self.root.geometry(f"{self.dim[0]}x{self.dim[1]}")

        # self.button = tk.Button(self.root, text="Spawn", command=self.buttonSpawn, width=100)
        # self.button.pack(padx=20, pady=20)

        self.canvas = tk.Canvas()
        self.canvas.pack(fill=tk.BOTH, expand=True)
    
    def gameloop(self):
        self.canvas.delete("all")
        self.antAction()
        self.drawFrame()
        self.root.after(1000, self.gameloop)

    def spawn(self, queen):
        spawned_ants = queen.spawn()
        if spawned_ants is not None:
            self.workers += spawned_ants

    def antAction(self):
        for ant in self.queens:
            self.spawn(ant)

        for ant in self.workers:
            pos = ant.pos
            targetTile = self.worldMap.map[ant.pos[1]][ant.pos[0]]
            if ant.move(targetTile):
                self.worldMap.map[pos[1]][pos[0]] = empty.Empty(targetTile.settings())
            if ant.dehidrate():
                self.workers.remove(ant)
    def drawFrame(self):
        def drawX(list):
            for ant in list:
                self.canvas.create_rectangle(
                    ant.pos[0] * 10, ant.pos[1] * 10, 
                    (ant.pos[0] + ant.size[0]) * 10, 
                    (ant.pos[1] + ant.size[1]) * 10,
                    fill="grey")
                
        create = self.canvas.create_line   

        for i, line in enumerate(self.worldMap.map):
            for j, pos in enumerate(line):
                create(j*10, i*10, (j+1)*10, (i)*10, fill=pos.color())

        drawX(self.queens)
        drawX(self.workers)
        
def main():
    game = Game()
    game.gameloop()
    game.root.mainloop()

if __name__ == "__main__":
    main()