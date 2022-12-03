from templatemethod.char_output import CharOutput
from templatemethod.table_output import TableOutput

def startMain():
    output1 = CharOutput('P')
    output2 = TableOutput("Hello World!")
    output1.output()
    print("")
    output2.output()

if __name__ == '__main__':
    startMain()