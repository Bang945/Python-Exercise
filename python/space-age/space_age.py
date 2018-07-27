

class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds;

    space_time = (1, 0.2408467, 0.61519726, 1.8808158, 11.862615, 29.447498, 84.016846, 164.79132)
    basic_time = 31557600.0

    def age(self, base):
        return float('%.2f' % (self.seconds / (self.basic_time * self.space_time[base])))

    def on_earth(self):
        return self.age(0)

    def on_mercury(self):
        return self.age(1)

    def on_venus(self):
        return self.age(2)

    def on_mars(self):
        return self.age(3)

    def on_jupiter(self):
        return self.age(4)

    def on_saturn(self):
        return self.age(5)

    def on_uranus(self):
        return self.age(6)

    def on_neptune(self):
        return self.age(7)