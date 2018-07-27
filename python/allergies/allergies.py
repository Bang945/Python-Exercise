class Allergies(object):
    allergies = {"eggs" : 1,
                 "peanuts" : 2,
                 "shellfish" : 4,
                 "strawberries" : 8,
                 "tomatoes" : 16,
                  "chocolate" : 32,
                  "pollen" : 64,
                  "cats" : 128}

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return self.score & self.allergies[item] != 0

    @property
    def lst(self):
        return list(filter(self.is_allergic_to, self.allergies.keys()))
        #  return [food for food, value in self.allergens.items()
        #        if self.flags & value]