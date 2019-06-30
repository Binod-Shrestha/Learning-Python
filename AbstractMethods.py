from abc import ABC,abstractmethod
class AnimalAbstractClass(ABC):
    #--------ABSTRACT METHODS----------
    @abstractmethod
    def fly(self):pass
    @abstractmethod
    def walk(self):pass
    @abstractmethod
    def swim(self):pass
