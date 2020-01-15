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
from logic.plan import Plan
from logic.template import Template
from logic.entry import Entry
from popmenu.popmenu import *

class PlanStructureWidget(FloatLayout):
    plan_t = ObjectProperty()
    entry_list = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plan = Plan("Heute")

    def add(self,eOT:Entry):
        eOT = self._addToPlan(eOT)
        self._addToEntryList(eOT)
        return eOT

    def _addToPlan(self,eOT):
        eOT = self.plan.add(eOT)
        self.plan_t.text = self.plan.getText()
        return eOT

    def _addToEntryList(self,eOT):
        self._appendEOT(eOT)

    def _getShow_popMenu(self,index):
        def showPopMenu():
            temp= self.plan.step_list[index]
            pM = PopMenu()
            pW = Popup(title=temp.theme,content=pM,size_hint=(0.8,0.8))
            
            pM.addEntries(temp)
            pM.addDeleteFunction(self._getRemoveEntry(index,dismiss_func=pW.dismiss))
            pM.addSplitFunction(self._get_get_splitFunc(index,dismiss_func=pW.dismiss))

            pW.open()
        return showPopMenu

    def _getRemoveEntry(self,index,dismiss_func=None):
        def removeEntry():
            self.removeElement(index)
            if not dismiss_func==None:
                dismiss_func()
        return removeEntry

    def updateEntryListLabels(self,index):
        self.entry_list.data = self.entry_list.data[:index]
        for i,e in enumerate(self.plan.step_list[index:],index):
            self._appendEOT(e)
   
    def _appendEOT(self,eOT:Entry):
        index = len(self.entry_list.data)
        func = self._getShow_popMenu if isinstance(eOT,Template) else self._getRemoveEntry
        dic = {'text': eOT.toString(),"on_press": func(index)}
        self.entry_list.data.append(dic)
    
    def _get_get_splitFunc(self,template_index,dismiss_func=None):
        def get_splitFunc(entry_index):
            def splitFunc():
                self.splitTemplate(template_index,entry_index)
                if not dismiss_func== None:
                    dismiss_func()
            return splitFunc
        return get_splitFunc
            
    def removeElement(self,index):
        self.entry_list.data.pop(index)
        self._removeFromPlan(index)
        self.updateEntryListLabels(index)
    
    def splitTemplate(self,template_index,split_index):
        self.plan.splitTemplate(template_index,split_index)
        self.updateEntryListLabels(template_index)

    def _removeFromPlan(self,index):
        self.plan.remove(index)
        self.plan_t.text = self.plan.getText()

class PlanStructureApp(App):
    def build(self):
        p = PlanStructureWidget()
        p.size = (500,500)
        t = Template("Template_Theme")
        t.add(Entry("00:05","test_entry_theme"))
        t.add(Entry("00:05","test_entry_theme2")) 

        p.add(t)
        return p

if __name__ == "__main__":
    PlanStructureApp().run()
