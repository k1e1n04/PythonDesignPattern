from gyudon.gyudon import Gyudon

class KoreanGyudon(Gyudon):
    def __init__(self):
        self.name = "Korean Gyudon"
        self.beef = "Korean beef"
        self.rice = "Korean rice"
        self.topping = []

    @staticmethod
    def serve():
        print("cooked Korean Gyudon")
        print("++++++++++++++++++++")

class KoreanCheeseGyudon(Gyudon):
    def __init__(self):
        self.name = "Korean Cheese Gyudon"
        self.beef = "Korean beef"
        self.rice = "Korean rice"
        self.topping = ["cheese"]

    @staticmethod
    def serve():
        print("cooked Korean Cheese Gyudon")
        print("++++++++++++++++++++")

class KoreanKimuchiGyudon(Gyudon):
    def __init__(self):
        self.name = "Korean Kimuchi Gyudon"
        self.beef = "Korean beef"
        self.rice = "Korean rice"
        self.topping = ["kimuchi","egg"]

    @staticmethod
    def serve():
        print("cooked Korean Kimuchi Gyudon")
        print("++++++++++++++++++++")