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
        data = self.template_List.rv_list.data
        for index,temp in enumerate(templates):
            data.append({'text': temp.toString(),
            "on_press": self.getAddTemp(temp)})
        self.time = (datetime.datetime.today()+datetime.timedelta(days=1)).strftime("%d.%m.%Y")
        self.t_name.text= self.time
        self.t_location.text=""

        self.loadPlan()
    
        keyboard = Window.request_keyboard(self._keyboard_released,self)
        keyboard.bind(on_key_down = self.on_key_down)

    def _keyboard_released(self):
        self.focus = False

    def on_key_down(self,window,keycode,text,modifiers):
        #print(keycode)
        if "ctrl" in modifiers:
            char = keycode[1]
            if  not char == None:
                switcher = {
                '#':self.plan_structure.updateWidgets,
                'spacebar':self.plan_structure.plan_update,
                's':self.savePlan,
                'l':self.loadPlan,
                'n':self.incrementDay,
                'p':self.decrementDay,
                't':self.setInputToTime
                }
                func = switcher.get(char) 
                if not func == None:
                    func()

    def incrementDay(self):
        (days,months,years) = self.time.split(".")
        new_time = datetime.date(int(years),int(months),int(days))+ datetime.timedelta(days=1)
        self.time = new_time.strftime("%d.%m.%Y")

    def decrementDay(self):
        (days,months,years) = self.time.split(".")
        new_time = datetime.date(int(years),int(months),int(days))- datetime.timedelta(days=1)
        self.time = new_time.strftime("%d.%m.%Y")

    def setInputToTime(self):
        self.t_name.text=self.time


    def getAddTemp(self,temp):
        def addTemp():
            temp_2 = self.plan_structure.add(temp)
        return addTemp    

    def savePlan(self):
        path = "plans\\"+self.t_name.text
        Load.save(path,self.plan_structure.plan.getFileText())

    def saveTemplate(self):
        name=self.t_name.text
        content= self.plan.theme+"\n"+self.plan_structure.plan_t.text
        Load.save("material\\"+name+""+"template",content)

    def loadPlan(self):
        path = "plans\\"+self.t_location.text + self.t_name.text
        plan = Load.parsePlan(Load.loadText(path))
        self.plan_structure.setPlan(plan)


class MainGUIApp(App):

    def build(self):
        return GUIGame()


if __name__ == '__main__':
    MainGUIApp().run()