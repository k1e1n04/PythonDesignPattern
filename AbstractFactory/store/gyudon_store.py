from abc import ABCMeta,abstractclassmethod

class GyudonStore(metaclass=ABCMeta):

    @abstractclassmethod
    def create_gyudon(self,gyudon_type):
        pass

    def order(self,gyudon_type):
        gyudon = self.create_gyudon(gyudon_type)

        gyudon.prepare()
        gyudon.serve()
        return gyudon

        
