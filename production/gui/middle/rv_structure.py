import kivy
kivy.require('1.11.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.recycleview import RecycleView
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

import sys
import os
sys.path.append(os.path.join("./production/logic"))
from plan import Plan
from template import Template
from entry import Entry


try:
    from middle.functionManager import FunctionManager
    from middle.planManager import PlanManager
except:
    from functionManager import FunctionManager
    from planManager import PlanManager


class RV_Structure(FloatLayout):
    
    rv_b_entries = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plan_manager = PlanManager(self.updateEntryListLabels)        
        self.func_manager = FunctionManager(self.plan_manager)

    def add_planManager(self,planManager):
        planManager.addUpdateStructure(self.updateEntryListLabels)
        self.plan_manager = planManager    
        self.func_manager.plan_manager = planManager
       
    def add_funcManager(self,func_manager):
        self.func_manager = func_manager

    def updateEntryListLabels(self,index=0):
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

class RV_StructureApp(App):
    
    def build(self):
        return RV_Templates()

if __name__ =="__main__":
    RVTApp().run()