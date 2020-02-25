try:
    from template import Template
    from entry import Entry
except:
    from .template import Template
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
            if not isinstance(e,Template):
                self.entries.append(e)
            else:
                self.addEntriesToList()
                self.formatted_list.append(e)
                self.entries = []

        self.addEntriesToList()

    def addEntriesToList(self):
        if self.enoughEntries():
            t = self.entriesToTemplate()
            self.formatted_list.append(t)
        else:
            self.formatted_list = self.formatted_list + self.entries

    def enoughEntries(self):
        return len(self.entries) > 1

    def entriesToTemplate(self):
        t = Template("...")
        t.start = self.entries[0].start
        for entry in self.entries:
            t.add(entry)
        return t

    def sortByStart(e):
        return e.start