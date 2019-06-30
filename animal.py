from AbstractMethods import AnimalAbstractClass
class Animal(AnimalAbstractClass):

    def __init__(self): pass

#---------GETTER/SETTERS-----------
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    def getAge(self):
        return self.__age
    def setAge(self, age):
        self.__age = age
    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color = color


#-------DOG CLASS WHICH INHERITS FROM ANIMAL CLASS
class Dog(Animal):
    def bark(self):
        print('Dog barks.')
    def fly(self):
        print('Dogs cannot fly.')
    def walk(self):
        print('Dog can walk.')
    def swim(self):
        print('Dog can swim')

# BIRD CLASS WHICH INHERITS FROM ANIMAL CLASS
class Bird(Animal):
    def fly(self):
        print('Birds can fly.')
    def walk(self):
        print('Birds walk with 2 legs.')
    def swim(self):
        print('Some birds can swim.')
    def sing(self):
        print('Birds can sing songs.')
# OBJECTS INSTANTIATIONS
dog = Dog()

#taking user's input
dogName = input('Enter Dog Name: ')
dogAge = int(input('Enter Dog Age: '))
dogColor = input('Enter Dog Color: ')

dog.setAge(f'I am {dogAge} years old.')
dog.setName(f"My Name is {dogName}.I am a dog.")
dog.setColor(f'I am {dogColor}')

print('')

bird = Bird()
birdName = input('Enter Bird Name:')
birdColor = input('Enter Bird Color:')
birdAge = int(input('Enter Bird Age:'))
bird.setName(f"My name is {birdName}.I am a bird.")
bird.setColor(f"I am {birdColor}")
bird.setAge(f'I am {birdAge} years old.')

print()
# print objects
print('*' * 25)
print(f'Name:{dog.getName()}\nAge:{dog.getAge()}\nColor:{dog.getColor()}')
print('*' * 25)
print(f'Name:{bird.getName()}\nAge:{bird.getAge()}\nColor:{bird.getColor()}')
print('*' * 25)

