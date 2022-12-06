from gyudon.gyudon import Gyudon

class JapaneseGyudon(Gyudon):
    def __init__(self):
        self.name = "Japanese Gyudon"
        self.beef = "Japanese beef"
        self.rice = "Japanese rice"
        self.topping = []

    @staticmethod
    def serve():
        print("cooked Japanese Gyudon")
        print("++++++++++++++++++++")

class JapaneseCheeseGyudon(Gyudon):
    def __init__(self):
        self.name = "Japanese Cheese Gyudon"
        self.beef = "Japanese beef"
        self.rice = "Japanese rice"
        self.topping = ["cheese"]

    @staticmethod
    def serve():
        print("cooked Japanese Cheese Gyudon")
        print("++++++++++++++++++++")

class JapaneseKimuchiGyudon(Gyudon):
    def __init__(self):
        self.name = "Japanese Kimuchi Gyudon"
        self.beef = "Japanese beef"
        self.rice = "Japanese rice"
        self.topping = ["kimuchi","egg"]

    @staticmethod
    def serve():
        print("cooked Japanese Kimuchi Gyudon")
        print("++++++++++++++++++++")


