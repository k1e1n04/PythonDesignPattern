# 抽象クラスモジュールをインポート
from abc import ABCMeta, abstractclassmethod

class AbstranctOutput(metaclass=ABCMeta):
    @abstractclassmethod
    def start(self):
        pass

    @abstractclassmethod
    def end(self):
        pass

    @abstractclassmethod
    def print(self):
        pass

    def output(self):
        # 文字列の出力回数を指定
        print_num = 10
        self.start()
        for _ in range(print_num):
            self.print()
        self.end()