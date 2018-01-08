class StudentFighter(object):

   
    def __init__(self, strength, health, name):
        self.strength = strength
        self.name = name
        self.health = health


Eunice = StudentFighter(strength=3, health=100, name="Kalu")
Katerina = StudentFighter(strength=5, health=100, name="David")

print(Eunice.name, Eunice.strength, Eunice.health)
print(Katerina.name, Katerina.strength, Katerina.health)