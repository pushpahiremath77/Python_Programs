class Bird:
    def fly(self):
        return "Bird flying"
    
class Airoplane:
    def fly(self):
        return "Airoplane is flying"
    
class Fish:
    def fly(Self):
        return "Fish is swimming"
    
def move_in_air(object):
    print(object.fly())

bird = Bird()
move_in_air(bird)

fish =Fish()
move_in_air(fish)

air = Airoplane()
move_in_air(air)