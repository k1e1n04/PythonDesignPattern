class Gyudon():
    def __init__(self):
        self.name:str = ""
        self.beef:str = ""
        self.rice:str = ""
        self.topping:list = []

    def get_name(self) -> str:
        return self.name

    def prepare(self):
        print("orderd " + self.get_name())
        print("work①: choose topping")
        print("chosen topping is: ",end="")
        for topping in self.topping:
            print(f"{topping} ")
        print()
        print("work②: serve")

    def choose_topping(self):
        return self.topping

    @staticmethod
    def serve():
        print("cooked Gyudon")
        print("++++++++++++++++++++")

    
