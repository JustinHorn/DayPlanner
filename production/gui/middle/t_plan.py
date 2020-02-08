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
    from middle.planManager import PlanManager
except:
    from planManager import PlanManager


class T_Plan(TextInput):
    textinput = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plan_manager = PlanManager(self.updateWidgets)        
    
    def add_planManager(self,planManager):
        planManager.addCommunication(self.updateWidgets)
        self.plan_manager = planManager    

    def getHotKeys(self):
        switcher = {}
        switcher['#']=self.updateWidgets
        switcher['spacebar']=self.update
        return switcher
    
    def updateWidgets(self):
        self.text = self.plan_manager.active.getText()

    def update(self):
        self.plan_manager.updateText(self.text)


class T_PlanApp(App):
    def build(self):
        p = Planner()
        p.size = (500,500)
        t = Template("Template_Theme")
        t.add(Entry("00:05","test_entry_theme"))
        t.add(Entry("00:05","test_entry_theme2")) 

        p.plan_manager.atOrSet(t)
        return p

if __name__ == "__main__":
    T_PlanApp().run()