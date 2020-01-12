from entry import Entry
import calcTime
class Template(Entry):


    def __init__(self,theme:str):
        super().__init__("00:00",theme)
        self.the_list = []


    def add(self,entry:Entry):
        self.the_list.append(entry)
        self.duration = calcTime.addTime(self.duration,entry.duration)


    def clone(self):
        clone = Template(self.theme)
        for e in self.the_list:
            clone.add(e.clone())
        return clone
