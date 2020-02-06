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
    from middle.planManager import PlanManager
except:
    from pop.popmenu import PopMenu
    from timeManager import TimeManager
    from functionManager import FunctionManager
    from planManager import PlanManager


class Planner(FloatLayout):
    textinput = ObjectProperty()
    rv_b_entries = ObjectProperty()
    t_theme = ObjectProperty()
    b_mode = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plan_manager = PlanManager(self.updateWidgets)        
        self.func_manager = FunctionManager(self.plan_manager,self.updateEntryListLabels)
    
    def add_planManager(self,planManager):
        self.plan_manager = planManager    
        self.time_manager = TimeManager(self.t_theme)
        self.func_manager = FunctionManager(self.plan_manager,self.updateEntryListLabels)


    def getHotKeys(self):
        if isinstance(self.plan_manager.active,Plan):
            switcher = self.time_manager.getHotKeys()
       
        switcher['spacebar']=self.update
        return switcher

    def changeMode(self):
        if isinstance(self.plan_manager.active,Plan):
            self.func_manager.source = self.plan_manager.active
            self.b_mode.text = "T/P"
        else:
            self.b_mode.text = "P/T"
        
        self.plan_manager.swapActive()
        self.updateWidgets()

    
    def updateWidgets(self):
        self.t_theme.text = self.plan_manager.active.theme
        self.textinput.text = self.plan_manager.active.getText()
        self.updateEntryListLabels(0)

    def update(self):
        self.plan_manager.active.theme = self.t_theme.text
        self.plan_manager.active.update(self.textinput.text)
        self.updateEntryListLabels(0)

    def updateEntryListLabels(self,index):
        self.rv_b_entries.data = self.rv_b_entries.data[:index]
        for e in self.plan_manager.active.step_list[index:]:
            self._appendEOT(e)

   
      
    def _appendEOT(self,eOT:Entry):
        index = len(self.rv_b_entries.data)
        f_m = self.func_manager
        func = f_m._getShow_popMenu if isinstance(eOT,Template) else f_m._getRemoveEntry
        if isinstance(self.plan_manager.active,Plan):
            dic = {'text': eOT.getStartThemeDuration(),"on_press": func(index)}
        else:
            dic = {'text': eOT.getThemeDuration(),"on_press": func(index)}
        self.rv_b_entries.data.append(dic)
            

class PlannerApp(App):
    def build(self):
        p = Planner()
        p.size = (500,500)
        t = Template("Template_Theme")
        t.add(Entry("00:05","test_entry_theme"))
        t.add(Entry("00:05","test_entry_theme2")) 

        p.plan_manager.atOrSet(t)
        return p

if __name__ == "__main__":
    PlannerApp().run()