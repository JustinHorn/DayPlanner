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

import sys
sys.path.append(".\\production\\logic")
sys.path.append("production\\gui\\middle")#needs to be connected! to a full path!

from plan import Plan
from template import Template
from rvTemplates import RV_Templates
from planStructure import PlanStructureWidget
import load

templates = load.loadTemplateDir("material\\test") #on testing

# templates = loadTemplateDir("material")

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
            data.append({'text': str(index) + " " +temp.info(),
            "on_press": self.getAddTemp(temp)})
        self.t_name.text=""
        self.t_location.text=""


    def getAddTemp(self,temp):
        def addTemp():
            temp_2 = self.plan_structure.add(temp)
        return addTemp    

    def savePlan(self):
        path = self.t_location.text + self.t_name.text
        load.save(path,self.plan_structure.plan_t.text)

    def saveTemplate(self):
        name=self.t_name.text
        load.save("material\\"+name+""+"template",self.plan_structure.plan_t.text)

    def loadPlan(self):
        path = self.t_location.text +"\\"+ self.t_name.text
        self.plan_structure.plan_t.text = load.loadPlan(path)


class MainGUIApp(App):

    def build(self):
        return GUIGame()


if __name__ == '__main__':
    MainGUIApp().run()