# 定義した抽象クラスをインポートする
from templatemethod.abstract_output import AbstranctOutput

# AbstranctOutput を継承
class TableOutput(AbstranctOutput):
    def __init__(self,char):
        self.__char = char
        self.__width = len(char)

    def start(self):
        # end 引数で末尾に出力するものを指定できる
        self._table_line()

    def end(self):
        # end 引数で末尾に出力するものを指定できる
        self._table_line()

    def print(self):
        # end 引数で末尾に出力するものを指定できる
        print(f'|{self.__char}|')

    def _table_line(self):
        print("*",end="")
        for _ in range(self.__width):
            print("-",end="")
        print("*")