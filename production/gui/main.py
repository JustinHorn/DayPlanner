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
from middle.planer import Planer
import Load

templates = Load.loadTemplateDir("material\\") #on testing
# templates = Load.loadTemplateDir("E:\\Python\\DayPlaner\\material")
#templates = loadTemplateDir("material")

class DayPlanerGUI(Widget):

    b_save = ObjectProperty()
    b_load = ObjectProperty()

    template_List = ObjectProperty()
    planer = ObjectProperty()

    t_name = ObjectProperty()
    t_location = ObjectProperty()

    PLANNING = 0
    TEMPLATING = 1

    def __init__(self):
        super().__init__()
        data = self.template_List.rv_list.data
        for index,temp in enumerate(templates):
            data.append({'text': temp.getThemeDuration(),
            "on_press": self.getAddTemp(temp)})
        self.time = (datetime.datetime.today()+datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        self.t_name.text= self.time
        self.loadPlan()
        self.mode = DayPlanerGUI.PLANNING

        keyboard = Window.request_keyboard(self._keyboard_released,self)
        keyboard.bind(on_key_down = self.on_key_down)
        self.planer.b_mode.on_press = self.changeMode

    def _keyboard_released(self):
        self.focus = False

    def on_key_down(self,window,keycode,text,modifiers):
        #print(keycode)
        if "ctrl" in modifiers:
            char = keycode[1]
            if  not char == None:
                switcher = {
                '#':self.planer.updateWidgets,
                'spacebar':self.planer.update,
                's':self.savePlan,
                'l':self.loadPlan,
                'n':self.incrementDay,
                'p':self.decrementDay,
                }
                func = switcher.get(char) 
                if not func == None:
                    func()

    def incrementDay(self):
        (days,months,years) = self.time.split(".")
        new_time = datetime.date(int(years),int(months),int(days))+ datetime.timedelta(days=1)
        self.time = new_time.strftime("%d.%m.%Y")
        self.setInputToTime()

    def decrementDay(self):
        (days,months,years) = self.time.split(".")
        new_time = datetime.date(int(years),int(months),int(days))- datetime.timedelta(days=1)
        self.time = new_time.strftime("%d.%m.%Y")
        self.setInputToTime()

    def setInputToTime(self):
        self.t_name.text=self.time

    def getAddTemp(self,temp):
        def addTemp():
            temp_2 = self.planer.atOrSet(temp)
        return addTemp    

    def savePlan(self):
        path = "plans\\"+self.t_name.text
        Load.save(path,self.planer.plan.getFileText())

    
    def loadPlan(self):
        path = "plans\\"+self.t_location.text + self.t_name.text
        plan = Load.parsePlan(Load.loadText(path))
        self.planer.setPlan(plan)

    def saveTemplate(self):
        path = "meterial\\"+self.t_name.text+"template"
        Load.save(path,self.planer.template.getFileText())

    def setTemplate(self,index):
        self.planer.setTemplate(template)

    def changeMode(self):
        t = self.planer.b_mode.text
        if t == "P/T":
            self.mode = DayPlanerGUI.TEMPLATING
            self.planer.changeMode()
            self.b_load.opacity = 0
        else:
            self.mode = DayPlanerGUI.PLANNING
            self.planer.changeMode()
            self.b_load.opacity = 1

class MainGUIApp(App):

    def build(self):
        return DayPlanerGUI()


if __name__ == '__main__':
    MainGUIApp().run()