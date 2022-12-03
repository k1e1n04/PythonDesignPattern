from abc import ABCMeta,abstractclassmethod

# 状態ごとに異なる振る舞いをするインタフェースを定めるスーパークラス
class State(metaclass=ABCMeta):

    @abstractclassmethod
    def handle(self):
        pass