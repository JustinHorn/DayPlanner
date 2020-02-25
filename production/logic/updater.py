"""A module that gives static helper functions to plan and main"""
try:
    from routine import Routine
    from entry import Entry
except:
    from .routine import Routine
    from .entry import Entry

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
        if isinstance(eOT,Routine):
            return self.routine_contain(eOT)
        else:
           return self.entry_contain(eOT)
    
    def entry_contain(self,entry):
        index = None
        if entry in self.entries:
            index = self.entries.index(entry)
        return (not index == None),index

    def getElement(self,index,element):
        if isinstance(element,Routine):
            ele = self.createNewRoutine(index,element)
        else:
            ele = self.entries[index] 

        ele.start= self.entries[index].start 
        return ele

    def createNewRoutine(self,index,old_routine):
        entries = self.entries[index:index+len(old_routine.step_list)]
        new_routine = Routine(old_routine.theme)
        new_routine.addAll(entries)
        # if i would have wrote better tests imediatly I would not have had to search +30m for this bugg 
        if not old_routine.step_list[-1].duration == "00:00": # might override real duration
            new_routine.step_list[-1].duration = old_routine.step_list[-1].duration
        return new_routine

    def routine_contain(self,routine):
        s_len =  len(routine.step_list) 
        stop = len(self.entries) - s_len +1
        for index,e in enumerate(self.entries[:stop] ):
            if routine.step_list == self.entries[index:index+s_len]:
                return True,index
        return False,None

    def shortenList(self,index,element):
        if isinstance(element,Routine):
            self.routine_shortenList(index,len(element.step_list))
        else:
            self.entries.pop(index)


    ###change Routine list
    def routine_shortenList(self,index,length):
        self.entries = self.entries[:index] + self.entries[index+length:]