from pathlib import Path

# rceiver 役
class FileOperator(object):
    def createFile(self,filename):
        Path(filename).touch()

    def changeFileMode(self,filename,permission):
        Path(filename).chmod(permission)