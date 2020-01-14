import kivy
kivy.require('1.11.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.recycleview import RecycleView
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import sys
sys.path.append(".\\production")
from plan import Plan
from template import Template
from entry import Entry
from popmenu.popmenu import *

class PlanStructureWidget(FloatLayout):
    plan_t = ObjectProperty()
    entry_list = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plan = Plan("Heute")

    def addTemplate(self,template:Template):
        temp = self.addToPlan(template)
        self.addToEntryList(temp)
     
        return temp

    def addToPlan(self,template):
            temp = self.plan.add(template)
            self.plan_t.text = self.plan.getText()
            return temp

    def addToEntryList(self,template):
        index = len(self.entry_list.data)
        self.entry_list.data.append({"text":str(index)+" "+template.toString(),
        "on_press": self.getShow_popMenu(index)
        })

    def getShow_popMenu(self,index):
        def showPopMenu():
            temp = self.plan.step_list[index]
            p = PopMenu(temp
            ,delete_press=self.getRemoveEntry(index)
            ,get_splitFunc=self.get_get_splitFunc(index))

            popupWindow = Popup(title=temp.theme,content=p,size_hint=(0.8,0.8))
            popupWindow.open()
        return showPopMenu


    def getRemoveEntry(self,index):
        def removeEntry():
            self.entry_list.data.pop(index)
            self.removeElement(index)
            self.updateEntryListLabels(index)
        return removeEntry

    def updateEntryListLabels(self,index):
        i = index
        for e in self.plan.step_list[index:]:
            if not (i >= len(self.entry_list.data)):
                self.entry_list.data[i]={'text': str(i) + " " +e.toString(),
                "on_press": self.getShow_popMenu(i)}
                i+=1
            else :
                self.entry_list.data.append({'text': str(i) + " " +e.toString(),
                "on_press": self.getShow_popMenu(i)})
                i+=1

    
    def get_get_splitFunc(self,template_index):
        def get_splitFunc(entry_index):
            def splitFunc():
                self.plan.splitTemplate(template_index,entry_index)
                self.updateEntryListLabels(template_index)
            return splitFunc
        return get_splitFunc

                


    def removeElement(self,index):
        self.plan.remove(index)
        self.plan_t.text = self.plan.getText()

class PlanStructureApp(App):
    def build(self):
        p = PlanStructureWidget()
        p.size = (500,500)
        t = Template("Template_Theme")
        t.add(Entry("00:05","test_entry_theme"))
        t.add(Entry("00:05","test_entry_theme2")) 

        p.addTemplate(t)
        return p

if __name__ == "__main__":
    PlanStructureApp().run()
