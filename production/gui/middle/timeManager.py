import datetime

class TimeManager():

    def __init__(self,textinput):
        self.time = (datetime.datetime.today()+datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        self.textinput = textinput

    def incrementDay(self):
        self.time  = (self.currentDayTime() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        self.textinput.text=self.time

    def decrementDay(self):
        self.time = (self.currentDayTime() - datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        self.textinput.text=self.time

    def getTime(self):
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