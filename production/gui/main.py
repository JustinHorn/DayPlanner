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
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window, Keyboard

import sys
import os
sys.path.append(os.path.join("./production/logic"))

from plan import Plan
from template import Template
from middle.rv_temp import RV_Templates
from middle.t_plan import T_Plan
from middle.rv_structure import RV_Structure

from middle.fileManager import FileManager
from middle.timeManager import TimeManager
from middle.planManager import PlanManager
from middle.functionManager import FunctionManager

try:
    os.mkdr(os.path.join("plans"))
except:
    print("error cant mkdr")

class DayPlannerGUI(Widget):

    b_save = ObjectProperty()
    b_load = ObjectProperty()
    rv_temp = ObjectProperty()
    t_plan = ObjectProperty()
    rv_struc = ObjectProperty()
    b_mode= ObjectProperty()
    t_theme= ObjectProperty()

    plan_manager = None
    file_manager = None
    func_manager = None
    time_manager = None

    def __init__(self):
        super().__init__()
        self.file_manager = FileManager("material/","plans/")
        self.file_manager.loadTemplates()
        self.time_manager = TimeManager(textinput=self.t_theme)
        self.plan_manager = PlanManager()
        self.func_manager = FunctionManager(self.plan_manager)

        self.rv_struc.add_planManager(self.plan_manager)
        self.rv_struc.add_funcManager(self.func_manager)

        self.t_plan.add_planManager(self.plan_manager)
        self.loadPlan()
        templates = self.file_manager.templates
        self.rv_temp.setTemps(templates,self.func_manager.getAddTemp)

        keyboard = Window.request_keyboard(self._keyboard_released,self)
        keyboard.bind(on_key_down = self.on_key_down)

    def updateTheme(self,text):
        if not self.plan_manager == None:
            self.plan_manager.updateTheme(text)

    def _keyboard_released(self):
        self.focus = False

    def on_key_down(self,window,keycode,text,modifiers):
        if "ctrl" in modifiers:
            char = keycode[1]
            if  not char == None:
                hotkeys = self.time_manager.getHotKeys()
                hotkeys = {**hotkeys,**self.t_plan.getHotKeys()}
                if self.b_mode.text == "P/T":
                    hotkeys['s']=self.savePlan
                    hotkeys['l']=self.loadPlan
                else:
                    hotkeys['s']=self.saveTemplate
                func = hotkeys.get(char) 
                if not func == None:
                    func()
     
    def savePlan(self):
        self.file_manager.savePlan(self.plan_manager.plan)
    
    def loadPlan(self):
        name = self.t_theme.text
        plan = self.file_manager.loadPlan(name)
        if not plan == None:
            self.plan_manager.setPlan(plan)
        
    def saveTemplate(self):
        self.file_manager.saveTemplate(self.plan_manager.template)  

    def changeMode(self):
        self.change()
        self.t_plan.updateWidgets()
        self.plan_manager.swapActive()

    def change(self):
        if self.b_mode.text == "P/T":
            self.b_mode.text = "T/P"
            self.b_load.opacity = 0
            self.b_save.text="save template"
            self.b_save.on_press = self.saveTemplate
        else:
            self.b_mode.text = "P/T"
            self.b_load.opacity = 1
            self.b_save.text="save plan"
            self.b_save.on_press = self.savePlan
            self.setTemps(self.file_manager.templates,self.func_manager.getAddTemp)


class MainGUIApp(App):

    def build(self):
        return DayPlannerGUI()

if __name__ == '__main__':
    MainGUIApp().run()