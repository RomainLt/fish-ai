from fishAgent import *
from badZone import *
from ihm import *
from random import *
from math import pi


class Ocean(BadZone):
    def __init__(self, _nbFishs, _max_width, _max_height):
        self.nbFishs = _nbFishs
        self.max_width = _max_width
        self.max_height = _max_height
        self.fishs = []
        self.obstacles = []

        random = Random()
        for nb in range(0, self.nbFishs):
            x = self.max_width * random.random()
            y = self.max_height * random.random()
            direction = 2 * pi * random.random()
            self.addFish(x, y, direction)

    # ajoute un fishAgent à la liste self.fishs
    def addFish(self, _x, _y, _direction):
        self.fishs.append(FishAgent(_x, _y, _direction))

    # appelle la méthode update (fishAgent) pour chaque fish de la liste self.fishs
    def update(self):
        for fish in self.fishs:
            fish.update(self.fishs, self.obstacles,
                        self.max_width, self.max_height)
        for obstacle in self.obstacles:
            if(obstacle.isDead()):
                self.obstacles.remove(obstacle)

    # ajout d'obstacles
    def addObstacle(self, _x, _y, _radius):
        self.obstacles.append(BadZone(_x, _y, _radius))
