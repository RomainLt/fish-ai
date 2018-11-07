from math import sqrt, cos, sin


class WorldObject:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    # retourne la distance entre self et worldObject
    def distanceTo(self, _worldObject):
        distanceX = _worldObject.x - self.x
        distanceY = _worldObject.y - self.y
        norme = sqrt((distanceX ** 2) + (distanceY ** 2))
        return norme

    # retourne la distance au carré entre self et worldObject
    def squareDistanceTo(self, _worldObject):
        result = self.distanceTo(_worldObject)
        return (result ** 2)
