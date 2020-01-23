class Entry():

    def __init__(self,duration:str,theme:str,start=None):
        self.duration = duration
        self.theme = theme
        self.start = start
        self.count = 1
    
    def clone(self):
        return Entry(self.duration,self.theme,self.start)
    
    def toString(self):
        return str(self.getText()+" "+ self.duration)

    def info(self):
        return str("Theme: "+self.theme+". Duration: "+self.duration+"\n")

    def getText(self):
        if self.start == None:
            return self.theme
        else:
            return str(self.start+" "+ self.theme)
    
    def __eq__(self, other):
        if isinstance(other,Entry):
            theme = other.theme.strip() == self.theme.strip()
            duration = (other.duration == self.duration) or(other =="00:00" or other.duration=="00:00")
            return theme and duration
        return False