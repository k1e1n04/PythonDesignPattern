from abc import ABCMeta, abstractclassmethod

class Observer(metaclass=ABCMeta):
    @abstractclassmethod
    def update(self, generator):
        pass