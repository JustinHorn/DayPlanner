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
from template import Template


class RV_Templates(FloatLayout):
    
    rv_list = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.templates = []

    def setTemps(self,temps,on_press):
        self.rv_list.data = {}
        for temp in temps:
                self.rv_list.data.append({'text': temp.getThemeDuration(),
                "on_press": on_press(temp)})



class RV_TempApp(App):
    
    def build(self):
        return RV_Templates()

if __name__ =="__main__":
    RVTApp().run()