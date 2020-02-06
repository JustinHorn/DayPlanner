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
from middle.rvTemplates import RV_Templates
from middle.planner import Planner
import load
from middle.fileManager import FileManager
from middle.timeManager import TimeManager
from middle.planManager import PlanManager
try:
    os.mkdr(os.path.join("plans"))
except:
    print("error cant mkdr")

class DayPlannerGUI(Widget):

    b_save = ObjectProperty()
    b_load = ObjectProperty()

    template_list = ObjectProperty()
    planner = ObjectProperty()

    def __init__(self):
        super().__init__()
        self.file_manager = FileManager("material/","plans/")
        self.file_manager.loadTemplates()

        self.updateTemplateList()
        self.plan_manager = PlanManager(self.planner.updateWidgets)

        self.planner.file_manager =self.file_manager
        self.planner.add_planManager(self.plan_manager)
        self.loadPlan()

        keyboard = Window.request_keyboard(self._keyboard_released,self)
        keyboard.bind(on_key_down = self.on_key_down)
        self.planner.b_mode.on_press = self.changeMode

    def updateTemplateList(self):
        self.template_list.rv_list.data = {}
        data = self.template_list.rv_list.data
        for temp in self.file_manager.templates:
            data.append({'text': temp.getThemeDuration(),
            "on_press": self.getAddTemp(temp)})

    def _keyboard_released(self):
        self.focus = False

    def on_key_down(self,window,keycode,text,modifiers):
        if "ctrl" in modifiers:
            char = keycode[1]
            if  not char == None:
                hotkeys = self.planner.getHotKeys()
                t = self.planner.b_mode.text
                if t == "P/T":
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
        name = self.planner.t_theme.text
        plan = self.file_manager.loadPlan(name)
        self.plan_manager.setPlan(plan)
        
    def saveTemplate(self):
        self.file_manager.saveTemplate(self.plan_manager.template)


    def getAddTemp(self,temp):
        def addTemp():
            temp_2 = self.plan_manager.atOrSet(temp)
        return addTemp    

    def changeMode(self):
        t = self.planner.b_mode.text
        if t == "P/T":
            self.b_load.opacity = 0
            self.b_save.text="save template"
            self.b_save.on_press = self.planner.saveTemplate
        else:
            self.updateTemplateList()
            self.b_load.opacity = 1
            self.b_save.text="save plan"
            self.b_save.on_press = self.planner.savePlan
        self.planner.changeMode()


class MainGUIApp(App):

    def build(self):
        return DayPlannerGUI()


if __name__ == '__main__':
    MainGUIApp().run()