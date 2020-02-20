import CalcTime

class Entry():

    def __init__(self,duration:str,theme:str,start=None):
        self.duration = duration
        self.theme = theme
        self.start = start
        self.count = 1
    
    def clone(self):
        return Entry(self.duration,self.theme,self.start)
    
    def getStartTheme(self):
        return str(self.start+" "+ self.theme)

    def getThemeDuration(self):
        return str(self.theme+" "+self.duration)
    
    def getStartThemeDuration(self):
        return str(self.start+" "+self.theme+" "+self.duration)

    def getEnd(self):
        return CalcTime.addTime(self.start,self.duration)       
    
    def __eq__(self, other):
        if isinstance(other,Entry):
            theme = other.theme.replace(" ","").split('#')[0] == self.theme.replace(" ","").split('#')[0]
            duration = (other.duration == self.duration) or(self.duration =="00:00" or other.duration=="00:00")
            return theme and duration
        return False