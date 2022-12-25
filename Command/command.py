from abc import ABCMeta,abstractclassmethod

# 命令の役
class Command(metaclass=ABCMeta):
    @abstractclassmethod
    def execute(self):
        pass

    @abstractclassmethod
    def display(self):
        pass


class FileTouchCommand(Command):
    def __init__(self,filename,receiverObj):
        self.__filename = filename
        self.__receiver = receiverObj

    def execute(self):
        self.__receiver.createFile(self.__filename)

    def display(self):
        print("% touch {0}".format(self.__filename))

class ChmodCommand(Command):
    def __init__(self,filename,permission,receiverObj):
        self.__filename = filename
        self.__permission = permission
        self.__receiver = receiverObj

    def execute(self):
        self.__receiver.changeFileMode(self.__filename, self.__permission)
        
    def display(self):
        permission = format(self.__permission, 'o')
        print("% chmod {0} {1}".format(permission, self.__filename))

    # invoker 役
class CompositeCommand(Command):
    def __init__(self):
        self.__cmds = []

    def append_cmd(self,cmd):
        self.__cmds.append(cmd)

    def execute(self):
        for cmd in self.__cmds:
            cmd.execute()

    def display(self):
        for cmd in self.__cmds:
            cmd.display()