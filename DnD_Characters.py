

class Adventurer(object):
    def __init__(self, name, voc, race, morality):
        self.name = name
        self.voc = voc
        self.race = race
        self.morality = morality

    def __repr__(self):
        return ("%s is a %s %s %s") % (self.name, self.morality, self.race, self.voc)
    



amanda = Adventurer('Althea', 'Wizard', '', 'Chaotic Good')
print (amanda)
