from entry import Entry
import CalcTime
import re
import ParseText

class Template(Entry):

    def __init__(self,theme:str):
        super().__init__("00:00",theme)
        self.step_list = []
        self.count = 0

    def len(self):
        return len(self.step_list)

    def add(self,entry:Entry):
        self.step_list.append(entry)
        self.duration = CalcTime.addTime(self.duration,entry.duration)
        self.count +=1

    def addAll(self,entries:list):
        for e in entries:
            self.add(e)

    def split(self,splitpoint):
        if splitpoint > len(self.step_list):
            print("error -0- template.py")
            pass #TODO: error should be thrown
        else :
            t1 = Template(self.theme+" 1/2")
            t2 = Template(self.theme+" 2/2")

            for e in self.step_list[:splitpoint]:
                t1.add(e.clone())

            for e in self.step_list[splitpoint:]:
                t2.add(e.clone())

            t1 = t1 if len(t1.step_list) > 1 else t1.step_list[0]

            t2 = t2 if len(t2.step_list) > 1 else t2.step_list[0]
            
            return t1,t2
    
    def remove(self,index):
        self.step_list.pop(index)

    def clone(self):
        clone = Template(self.theme)
        for e in self.step_list:
            clone.add(e.clone())
        return clone

    def __eq__(self, other):
        if isinstance(other,self.__class__):
            s_l = other.step_list
            if not len(s_l) == len(self.step_list):
                return False
            for eO,eS in zip(s_l,self.step_list):
                if not eO == eS:
                    return False
            return True
        return False  

    #TODO: enforce Textformat
    def update(self,text):
        self.duration = "00:00"
        self.step_list = []
        self.count = 0
        entries = ParseText.parseTextToTemplateEntries(text)
        for e in entries:
            self.add(e)
    

    def templateToText(self,startTime="00:00"):
        step_list = self.step_list
        text = ""
        for i,e in enumerate(step_list):
            text += startTime+" "+e.theme +"\n"
            startTime = CalcTime.addTime(startTime,e.duration)
        return text,startTime

    def getText(self):
        """ Used in planer to display duration at the start of each line"""
        text = ""
        for e in self.step_list:
            text += e.duration+" "+e.theme +"\n"
        return text
    
    def getFileText(self):
        return self.theme+"\n" + self.getText()


