from datetime import datetime as dt
import os

class Logger:
    def __init__(self):
        pass

    def getStrCurrentTime(self, format):
        return dt.now().strftime(format)
    
    def debug(self, st):
        fullSt = self.getStrCurrentTime("%d-%m-%Y %H-%M-%S") + "\t: " + st + "\n"
        curFileName = self.getStrCurrentTime("%d-%m %H") + ".txt"
        path = "Log/" + curFileName
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok = True)

        self.curFile = open(path, "a")
        self.curFile.write(fullSt)
        self.curFile.close()
    
