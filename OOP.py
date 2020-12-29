
#parent class
class Organism:
    name = 'unknown'
    species = 'unknown'
    legs = None
    arms = None
    dna = "sequence A"
    origin = "unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nspecies: {}\nlegs: {}\narms: {}\ndna: {}\norigin: {}\ncarbon based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

#child class instance
class Human(Organism):
    name = "macguyver"
    species = 'homosapien'
    legs = 2
    arms = 2
    origin = 'earth'

    def ingenuity(self):
        msg= "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg

#another child class instance
class Dog(Organism):
    name = "spot"
    species = "canine"
    legs = 4
    arms = 0
    dna = "sequence B"
    origin = 'earth'
    
    def bit(self):
        msg="\nEmits a loud, menacing growl and bites down ferociously on its target!"
        return msg

    
#another child class instance
class Bacterium(Organism):  
    name = "x"
    species = "bacteria"
    legs = 0
    arms = 0
    dna = "sequence c"
    origin = 'earth'
    
    def replication(self):
        msg="\nthe cells begin to divide and mulitply into two seperate organisms!"
        return msg


    

if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())
    dog = Dog()
    print(dog.information())
    print(dog.bit())
    bact = Bacterium()
    print(bact.information())
    print(bact.replication())
    
