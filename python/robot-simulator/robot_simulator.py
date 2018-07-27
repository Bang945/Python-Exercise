# Globals for the bearings
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y


    def __getattr__(self, coordinates):
        return (self.x, self.y)


    def advance(self):
        if self.bearing % 2 == 1:
            self.y += 2 - self.bearing
        else:
            self.x += 1 - self.bearing
        print(self.x, ":", self.y)


    def turn_left(self):
        self.bearing = (self.bearing + 1) % 4


    def turn_right(self):
        self.bearing = (self.bearing + 3) % 4


    def simulate(self, path):
        for p in path:
            if p == 'A':
                self.advance()
            elif p == 'R':
                self.turn_right()
            elif p == 'L':
                self.turn_left()

