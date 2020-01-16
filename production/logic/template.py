from entry import Entry
import calcTime
class Template(Entry):

    def __init__(self,theme:str):
        super().__init__("00:00",theme)
        self.step_list = []

    def add(self,entry:Entry):
        self.step_list.append(entry)
        self.duration = calcTime.addTime(self.duration,entry.duration)

    def split(self,splitpoint):
        if splitpoint > len(self.step_list):
            print("error -0- template.py")
            pass # error should be thrown
        else :
            t1 = Template(self.theme+" 1/2")
            t2 = Template(self.theme+" 2/2")

            for e in self.step_list[:splitpoint]:
                t1.add(e.clone())

            for e in self.step_list[splitpoint:]:
                t2.add(e.clone())

            if len(t1.step_list) == 1:
                t1 = t1.step_list[0]

            if len(t2.step_list) == 1:
                t2 = t2.step_list[0]
            
            return t1,t2

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
