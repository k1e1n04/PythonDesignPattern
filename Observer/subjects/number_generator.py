from abc import ABCMeta, abstractclassmethod

# Subject 役
class NumberGenerator(metaclass=ABCMeta):
    def __init__(self):
        self.__observers = []

    def addObserver(self,observer):
        self.__observers.append(observer)

    def deleteObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObserver(self):
        for observer in self.__observers:
            observer.update(self)

    @abstractclassmethod
    def getNumber(self):
        pass

    @abstractclassmethod
    def execute(self):
        pass