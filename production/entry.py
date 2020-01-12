class Entry():

    def __init__(self,duration:str,theme:str,start=None):
        self.duration = duration
        self.theme = theme
        self.start = start
    
    def clone(self):
        return Entry(self.duration,self.theme,self.start)
    
    def toString(self):
        return str(str(self.start)+"|"+self.theme+"|"+self.duration+"\n")

    def info(self):
        return str(self.theme+"|"+self.duration+"\n")

