from abc import ABCMeta, abstractmethod
class Pet():
    __metaclass__=ABCMeta
    @abstractmethod
    def speak(self):
        super().__init__()
        return 'no sound'
    
class Cat(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('meow', random(50, width-70), random(50, height-50))
        return 'meow'
    def __sub__(self, other):
        return self.name[0]+ ' od ' +other.name[0]
    
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
         text('woof', random(50, width-70), random(50, height-50))
         return 'woof'
    def __add__(self, other):
        return self.name[0]+ ' i ' + other.name[0]
    
class Cow(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('muuu', random(50, width-70), random(50, height-50))
        return 'muuu'
    
def setup():
    size(400,400)
    brrr = loadImage('brrr.jpg')
    image(brrr, 0, 0, height, width)
    textSize(20)
    rex = Dog('Rex')
    benio = Dog('Benio')
    mucha = Dog('Mucha')
    skrypcik = Cat('Skrypcik')
    oskar = Cat('Oskar')
    helenka = Cow('Helenka')
    global list_of_pets
    list_of_pets = [rex, benio, mucha, skrypcik, oskar, helenka]
    print(rex + benio)
    print(skrypcik - oskar)

def draw():
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak()
        
# 1,5pkt - brak nadpisania odejmowania, to było w linku do referencji, __sub__ - od substract
