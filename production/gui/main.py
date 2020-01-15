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

import sys
sys.path.append(".\\production\\logic")
sys.path.append("production\\gui\\middle")

from plan import Plan
from template import Template
from middle.rvTemplates import RV_Templates
from middle.planStructure import PlanStructureWidget
from load import *

templates = loadTemplateDir("material\\test")


class GUIGame(Widget):

    template_List = ObjectProperty()
    plan_structure = ObjectProperty()
    def __init__(self):
        super().__init__()
        data = self.template_List.data
        for index,temp in enumerate(templates):
            data.append({'text': str(index) + " " +temp.info(),
            "on_press": self.getAddTemp(temp)})

    def getAddTemp(self,temp):
        def addTemp():
            temp_2 = self.plan_structure.add(temp)
        return addTemp


class MainGUIApp(App):

    def build(self):
        return GUIGame()


if __name__ == '__main__':
    MainGUIApp().run()