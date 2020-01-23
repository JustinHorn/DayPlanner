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

import datetime

import sys
sys.path.append(".\\production\\logic")
# sys.path.append("production\\gui\\middle")#needs to be connected! to a full path!

from plan import Plan
from template import Template
from middle.rvTemplates import RV_Templates
from middle.planStructure import PlanStructureWidget
import Load

templates = Load.loadTemplateDir("material\\test") #on testing
# templates = Load.loadTemplateDir("E:\\Python\\DayPlaner\\material")
#templates = loadTemplateDir("material")

class GUIGame(Widget):

    b_savePlan = ObjectProperty()
    b_saveTemplate = ObjectProperty()
    b_loadPlan = ObjectProperty()

    template_List = ObjectProperty()
    plan_structure = ObjectProperty()

    t_name = ObjectProperty()
    t_location = ObjectProperty()

    def __init__(self):
        super().__init__()
        data = self.template_List.data
        for index,temp in enumerate(templates):
            data.append({'text': temp.toString(),
            "on_press": self.getAddTemp(temp)})
        self.t_name.text= (datetime.datetime.today()+datetime.timedelta(days=1)).strftime("%d.%m.%Y.txt")
        self.t_location.text=""

        self.loadPlan()
        

        keyboard = Window.request_keyboard(self._keyboard_released,self)
        keyboard.bind(on_key_down = self.on_key_down)

    def _keyboard_released(self):
        self.focus = False

    def on_key_down(self,window,keycode,text,modifiers):
        # print(keycode)
        # print(modifiers)
        if "ctrl" in modifiers and keycode[1]=='u':
            self.plan_structure.plan_update() 
        elif "ctrl" in modifiers and keycode[1]=='s':
            self.savePlan()
        elif "ctrl" in modifiers and keycode[1]=='n':
            self.savePlan()


    def getAddTemp(self,temp):
        def addTemp():
            temp_2 = self.plan_structure.add(temp)
        return addTemp    

    def savePlan(self):
        path = "plans\\"+self.t_name.text
        Load.save(path,self.plan_structure.plan.getFileText())

    def saveTemplate(self):
        name=self.t_name.text
        Load.save("material\\"+name+""+"template",self.plan_structure.plan_t.text)

    def loadPlan(self):
        path = "plans\\"+self.t_location.text + self.t_name.text
        self.plan_structure.plan = Load.parsePlan(Load.loadText(path))
        self.plan_structure.updateWidgets()


class MainGUIApp(App):

    def build(self):
        return GUIGame()


if __name__ == '__main__':
    MainGUIApp().run()