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
import os
sys.path.append(os.path.join("./production/logic"))


from plan import Plan
from template import Template
from entry import Entry
try:
    from .pop.popmenu import PopMenu
    from middle.timeManager import TimeManager
    from middle.functionManager import FunctionManager
except:
    from pop.popmenu import PopMenu
    from timeManager import TimeManager
    from functionManager import FunctionManager


class Planner(FloatLayout):
    textinput = ObjectProperty()
    rv_b_entries = ObjectProperty()
    t_theme = ObjectProperty()
    b_mode = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plan = Plan("Heute")
        self.template = Template("Template Theme")
        self.source = self.plan        
        self.time_manger = TimeManager(self.t_theme)
        self.func_manager = FunctionManager(self.plan,self.updateEntryListLabels,
        self.splitTemplate,self.removeElement)
    
    def getHotKeys(self):
        if isinstance(self.source,Plan):
            switcher = self.time_manger.getHotKeys()
            switcher['s']=self.savePlan
            switcher['l']=self.loadPlan
        else:
            switcher= {}
            switcher['s']=self.saveTemplate

        switcher['spacebar']=self.update
        return switcher

    def changeMode(self):
        if isinstance(self.source,Plan):
            self.source = self.template
            self.func_manager.source = self.template
            self.b_mode.text = "T/P"
        else:
            self.source = self.plan
            self.b_mode.text = "P/T"
        
        self.updateWidgets()


    def update(self):
        self.source.theme = self.t_theme.text
        self.source.update(self.textinput.text)
        self.updateEntryListLabels(0)

    def setPlan(self,plan):
        self.plan = plan
        self.source =plan
        self.updateWidgets()
        self.func_manager.plan = plan
        self.func_manager.source = plan

    def atOrSet(self,eOT:Entry):
        if isinstance(self.source,Plan):
            return self._add(eOT)
        else:
            return self.setTemplate(eOT)

    def setTemplate(self,temp):
        self.source = temp
        self.updateWidgets()
        self.source = self.template
        self.update()
        return temp

    def _add(self,eOT:Entry):
        eOT = self._addToPlan(eOT)
        index = len(self.plan.step_list)
        self.updateEntryListLabels(index)
        return eOT

    def updateEntryListLabels(self,index):
        self.rv_b_entries.data = self.rv_b_entries.data[:index]
        for e in self.source.step_list[index:]:
            self._appendEOT(e)

    def _addToPlan(self,eOT):
        eOT = self.plan.add(eOT)
        self.textinput.text = self.plan.getText()
        return eOT
      
    def _appendEOT(self,eOT:Entry):
        index = len(self.rv_b_entries.data)
        f_m = self.func_manager
        func = f_m._getShow_popMenu if isinstance(eOT,Template) else f_m._getRemoveEntry
        if isinstance(self.source,Plan):
            dic = {'text': eOT.getStartThemeDuration(),"on_press": func(index)}
        else:
            dic = {'text': eOT.getThemeDuration(),"on_press": func(index)}
        self.rv_b_entries.data.append(dic)
            
    def splitTemplate(self,template_index,split_index):
        self.source.splitTemplate(template_index,split_index) # must be plan
        self.updateEntryListLabels(template_index)

    def removeElement(self,index):
        self.source.remove(index)
        self.textinput.text = self.source.getText()
        self.updateEntryListLabels(index)

    def updateWidgets(self):
        self.t_theme.text = self.source.theme
        self.textinput.text = self.source.getText()
        self.updateEntryListLabels(0)

    def savePlan(self):
        self.file_manager.savePlan(self.plan)
    
    def loadPlan(self):
        name = self.t_theme.text
        plan = self.file_manager.loadPlan(name)
        self.setPlan(plan)
        
    def saveTemplate(self):
        self.file_manager.saveTemplate(self.template)


class PlannerApp(App):
    def build(self):
        p = Planner()
        p.size = (500,500)
        t = Template("Template_Theme")
        t.add(Entry("00:05","test_entry_theme"))
        t.add(Entry("00:05","test_entry_theme2")) 

        p._add(t)
        return p

if __name__ == "__main__":
    PlannerApp().run()