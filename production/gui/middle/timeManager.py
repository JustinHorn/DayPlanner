import datetime

class TimeManager():

    def __init__(self,textinput=None):
        self.time = (datetime.datetime.today()+datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        self.textinput = textinput
        self.getTime()

    def incrementDay(self):
        self.time  = (self.currentDayTime() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        self.getTime()

    def decrementDay(self):
        self.time = (self.currentDayTime() - datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        self.getTime()

    def getTime(self):
        if not self.textinput == None:
            self.textinput.text=self.time

    def currentDayTime(self):
        (days,months,years) = self.time.split(".")
        return datetime.date(int(years),int(months),int(days))

    def getHotKeys(self):
        switcher = {
        'n':self.incrementDay,
        'p':self.decrementDay,
        't':self.getTime}
        return switcher