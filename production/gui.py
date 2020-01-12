import kivy
kivy.require('1.11.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import sys
sys.path.append(".")
from production.plan import Plan
from production.template import Template
from production.load import *

templates = loadTemplateDir("material\\test")


class GUIGame(Widget):

    template_List = ObjectProperty()
    structure_List= ObjectProperty()
    plan_t = ObjectProperty()
    def __init__(self):
        super().__init__()
        data = self.template_List.data
        for index,button in enumerate(data):
            button["on_press"] = self.getAddTemp(index)

    def getAddTemp(self,index:int):
        def addTemp():
            tem = templates[index]
            temp_2 = self.plan_t.addTemplate(tem)
            self.structure_List.addEntry(temp_2,self.plan_t)
        return addTemp

class RV_Templates(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template = []
        [self.addTemplate(temp) for temp in templates]

    def addTemplate(self,template:Template):
        index = str(len(self.data))
        self.data.append({"text":index+" "+ template.theme+" "+template.duration})


class PlanWidget(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plan = Plan("Heute")

    def addTemplate(self,template:Template):
        temp = self.plan.add(template)
        self.text = self.plan.getText()
        return temp

    def removeElement(self,index):
        self.plan.remove(index)
        self.text = self.plan.getText()

class RV_Structure(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def addEntry(self,eOT:Entry,planW:PlanWidget):
        index = len(self.data)
        self.data.append({"text":str(index)+" "+eOT.toString(),
        "on_press": self.getRemoveEntry(index,planW)
        })
    
    def getRemoveEntry(self,index,planW:PlanWidget):
        def removeEntry():
            self.data.pop(index)
            planW.removeElement(index)
            self.updateStructureLabels(index,planW)
        return removeEntry

    def updateStructureLabels(self,index,planW:PlanWidget):
        i = index
        for e in self.data[index:]:
            text = e['text']
            e['text'] = str(i) + " " +planW.plan.the_list[i].toString()
            e["on_press"] = self.getRemoveEntry(i,planW)
            i+=1



class GUIApp(App):

    def build(self):
        return GUIGame()


if __name__ == '__main__':
    GUIApp().run()