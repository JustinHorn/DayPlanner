"""A module that gives static helper functions to plan and main"""
from template import Template
from entry import Entry

class Updater():

    def __init__(self,plan_list,entries):
        self.plan_list = plan_list
        self.entries = entries[:]

    def update(self):
        merge = self.mergeListToEntries()
        return merge

    def mergeListToEntries(self):
        merge = []
        for e in self.plan_list:
            contains, index = self.doesEntryListContain(e)
            if contains:
                new_element = self.getElement(index,e)
                self.shortenList(index,e)
                merge.append(new_element)

        merge = merge + self.entries
        return merge

    def doesEntryListContain(self,eOT:Entry):
        if isinstance(eOT,Template):
            return self.template_contain(eOT)
        else:
           return self.entry_contain(eOT)
    
    def entry_contain(self,entry):
        index = None
        if entry in self.entries:
            index = self.entries.index(entry)
        return (not index == None),index

    def getElement(self,index,element):
        if isinstance(element,Template):
            ele = self.createNewTemplate(index,element)
        else:
            ele = self.entries[index] 

        ele.start= self.entries[index].start 
        return ele

    def createNewTemplate(self,index,old_temp):
        entries = self.entries[index:index+len(old_temp.step_list)]
        new_temp = Template(old_temp.theme)
        new_temp.addAll(entries)
        new_temp.step_list[-1].duration = old_temp.step_list[-1].duration
        return new_temp

    def template_contain(self,template):
        s_len =  len(template.step_list) 
        stop = len(self.entries) - s_len +1
        for index,e in enumerate(self.entries[:stop] ):
            if template.step_list == self.entries[index:index+s_len]:
                return True,index
        return False,None

    def shortenList(self,index,element):
        if isinstance(element,Template):
            self.template_shortenList(index,len(element.step_list))
        else:
            self.entries.pop(index)


    ###change template list
    def template_shortenList(self,index,length):
        self.entries = self.entries[:index] + self.entries[index+length:]