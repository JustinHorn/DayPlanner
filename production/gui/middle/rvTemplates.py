import kivy
kivy.require('1.11.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.recycleview import RecycleView
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty


import sys
sys.path.append(".\\production\\logic")
from template import Template


class RV_Templates(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.templates = []

    def addTemplate(self,template:Template):
        index = str(len(self.data))
        self.data.append({"text":index+" "+ template.theme+" "+template.duration})
        self.templates.append(template)

class RVTApp(App):
    pass