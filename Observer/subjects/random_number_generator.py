from subjects.number_generator import NumberGenerator
import random

class RandomNumberGenerator(NumberGenerator):
    def __init__(self):
        self.__number = 0
        super(RandomNumberGenerator, self).__init__()

    def getNumber(self):
        return self.__number
    
    def execute(self):
        loop_num = 20
        for _ in range(loop_num):
            self.__number = random.randint(0,49)
            self.notifyObserver()