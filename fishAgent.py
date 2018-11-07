from worldObject import *
import math
import random


class FishAgent(WorldObject):
    STEP = 2.0  # pas de déplacement
    DISTANCE_MIN = 10.0
    DISTANCE_MAX = 30.0
    SQUARE_DISTANCE_MIN = 100.0
    SQUARE_DISTANCE_MAX = 900.0
    WALL_AVOID = 0.3

    def __init__(self, _x, _y, _direction):
        self.x = _x
        self.y = _y
        self.vx = cos(_direction)
        self.vy = sin(_direction)
        color = ['blue', 'green', 'orange', 'black', 'red', 'grey', 'purple']
        i = random.randint(0, 6)
        self.color = color[i]

    # fait évoluer la position de l'agent (x,y) -> vitesse vx et vy + STEP
    def updatePosition(self):
        self.x += self.vx * self.STEP
        self.y += self.vy * self.STEP

    # normalise les coordonnées x et y avec la vitesse
    def normalise(self):
        norme = sqrt((self.vx ** 2) + (self.vy ** 2))
        self.vx = self.vx/norme
        self.vy = self.vy/norme

    # retourne vrai si la distance de self avec un autre agent est dans la zone NEAR
    def near(self, _fishAgent):
        distance = self.distanceTo(_fishAgent)
        if(distance > self.DISTANCE_MIN and distance < self.DISTANCE_MAX):
            return True
        return False

    # appelle la méthode updatePosition de self, point d'entrée comportement de l'agent
    def update(self, _fishs, _obstacles, _max_width, _max_height):
        self.updatePosition()
        self.avoidWall(0, _max_width, 0, _max_height)
        self.avoidFishs(_fishs)
        self.computeAverageDirection(_fishs)
        self.avoidObstacle(_obstacles)

    # modifie la vitesse et la position de l'agent lorsqu'il s'approche d'un mur
    def avoidWall(self, _wallXMin, _wallXMax, _wallYMin, _wallYMax):
        if(self.x < _wallXMin + 10):
            self.vx += self.WALL_AVOID
        if(self.x > _wallXMax - 10):
            self.vx -= self.WALL_AVOID
        if(self.y < _wallYMin + 10):
            self.vy += self.WALL_AVOID
        if(self.y > _wallYMax - 10):
            self.vy -= self.WALL_AVOID

        self.normalise()

    # modifie la vitesse de l'agent lorsqu'il s'approche trop d'un autre agent
    def avoidFishs(self, _fishs):
        for fish in _fishs:
            if fish != self:
                # vecteur
                x = fish.x - self.x
                y = fish.y - self.y
                # distance au carré
                distance = (x ** 2) + (y ** 2)
                if(distance < self.SQUARE_DISTANCE_MIN):
                    self.vx -= x
                    self.vy -= y
                    self.normalise()

    # modifie la vitesse de l’agent en fonction de la direction de ses proches voisins
    def computeAverageDirection(self, _fishs):
        vxAverage = 0
        vyAverage = 0
        countFish = 0
        for fish in _fishs:
            if fish != self:
                if(self.near(fish)):
                    vxAverage += fish.vx
                    vyAverage += fish.vy
                    countFish += 1

        if(countFish > 0):
            moyX = vxAverage / countFish
            moyY = vyAverage / countFish
            self.vx += moyX
            self.vy += moyY
            self.normalise()

    # recherche l'objet le plus proche de l'agent et modifie la vitesse de l'agent s'il s'approche trop
    def avoidObstacle(self, _obstacles):
        for obstacle in _obstacles:
            # distance entre l'obstacle et l'agent
            x = obstacle.x - self.x
            y = obstacle.y - self.y
            # distance au carré
            distance = (x ** 2) + (y ** 2)
            if(distance < self.SQUARE_DISTANCE_MIN):
                self.vx -= x
                self.vy -= y
                self.normalise()
