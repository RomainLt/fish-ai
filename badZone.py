from worldObject import *
import math
import random


class BadZone:
    def __init__(self, _x, _y, _radius=10, _livetime=200):
        self.x = _x
        self.y = _y
        self.livetime = _livetime
        self.radius = _radius

    def update(self):
        self.livetime -= 1

    def isDead(self):
        self.update()
        if(self.livetime < 0):
            return True
        return False
