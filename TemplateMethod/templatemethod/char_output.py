# 定義した抽象クラスをインポートする
from templatemethod.abstract_output import AbstranctOutput

# AbstranctOutput を継承
class CharOutput(AbstranctOutput):
    def __init__(self,char):
        self.__char = char

    def start(self):
        # end 引数で末尾に出力するものを指定できる
        print("【", end="")

    def end(self):
        # end 引数で末尾に出力するものを指定できる
        print("】", end="")

    def print(self):
        # end 引数で末尾に出力するものを指定できる
        print(self.__char,end="")