from worldObject import *
from fishAgent import *
from ocean import *
from tkinter import *
import random
import math


class Ihm:
    AGENT_LENGTH = 10

    def __init__(self, environment):
        # l’océan dans notre cas
        self.environment = environment
        fen = Tk()
        self.canvas = Canvas(fen, width=self.environment.max_width,
                             height=self.environment.max_height, bg='white', bd=0)
        self.canvas.pack()
        self.fen = fen
        self.canvas.bind_all("a", self.addFish)  # attacher une touche
        self.canvas.bind("<Button-3>", self.addFish)  # attacher la souris
        self.canvas.bind("<Button-1>", self.addObstacle)
        self.fen.after(1000, self.update)  # lancer la boucle principale
        self.fen.mainloop()

    def addFish(self, event):
        self.environment.addFish(
            event.x, event.y, random.random()*2*math.pi)

    def addObstacle(self, event):
        self.environment.addObstacle(
            event.x, event.y, 10)

    def drawFish(self, _fishAgent):
        self.canvas.create_line(_fishAgent.x, _fishAgent.y,
                           _fishAgent.x - (_fishAgent.vx * self.AGENT_LENGTH), _fishAgent.y - (_fishAgent.vy * self.AGENT_LENGTH), fill=_fishAgent.color)

    def drawObstacle(self, _obstacle):
        self.canvas.create_oval(_obstacle.x, _obstacle.y,
                           _obstacle.x + _obstacle.radius, _obstacle.y + _obstacle.radius, fill='black')

    def draw(self):
        self.canvas.delete(ALL)
        for fish in self.environment.fishs:
            self.drawFish(fish)
        for obstacle in self.environment.obstacles:
            self.drawObstacle(obstacle)

    def update(self):
        self.environment.update()
        self.draw()
        self.fen.after(25, self.update)

# Lancer le programme
if __name__ == "__main__":
    ocean = Ocean(50, 500, 500)
    ihm = Ihm(ocean)