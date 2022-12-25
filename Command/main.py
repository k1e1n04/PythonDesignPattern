import sys
from command import *
from receiver import *

def startMain(filename, permission):
    recv = FileOperator()
    cc = CompositeCommand()
    cc.append_cmd(FileTouchCommand(filename, recv))
    cc.append_cmd(ChmodCommand(filename, permission, recv))
    cc.execute()
    cc.display()


if __name__ == "__main__":
    startMain(sys.argv[1], int(sys.argv[2], 8))