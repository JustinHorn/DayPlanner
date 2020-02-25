try:
    from routine import Routine
    from entry import Entry
except:
    from .routine import Routine
    from .entry import Entry

class FormatStructure():

    def __init__(self,step_list:list):
        self.step_list = step_list
        self.formatted_list = []
        self.entries = []

    def format(self):
        self.step_list.sort(key=FormatStructure.sortByStart)
        self.formatList()
        return self.formatted_list

    def formatList(self):
        for e in self.step_list:
            if not isinstance(e,Routine):
                self.entries.append(e)
            else:
                self.addEntriesToList()
                self.formatted_list.append(e)
                self.entries = []

        self.addEntriesToList()

    def addEntriesToList(self):
        if self.enoughEntries():
            r = self.entriesToRoutine()
            self.formatted_list.append(r)
        else:
            self.formatted_list = self.formatted_list + self.entries

    def enoughEntries(self):
        return len(self.entries) > 1

    def entriesToRoutine(self):
        r = Routine("...")
        r.start = self.entries[0].start
        for entry in self.entries:
            r.add(entry)
        return r

    def sortByStart(e):
        return e.start