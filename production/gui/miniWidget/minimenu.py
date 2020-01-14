import kivy
kivy.require('1.11.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.recycleview import RecycleView
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty


import sys
sys.path.append(".\\production")
from plan import Plan
from template import Template
from entry import Entry

class PopMenu(FloatLayout):

    recycle = ObjectProperty() 
    button = ObjectProperty()

    def __init__(self,template:Template,on_press=None):
        super().__init__()
        for e in template.step_list:
            self.addToStucture(e)
        self.button.on_press = on_press

    def addToStucture(self,entry,on_press=None):
        index = len(self.recycle.data)
        if on_press == None:
            self.recycle.data.append({"text":str(index)+" "+entry.toString()
            })
        else:
            self.recycle.data.append({"text":str(index)+" "+entry.toString(),
            "on_press":on_press})

class MiniMenuApp(App):
    def build(self):
        return PopMenu(Template("l"))

if __name__ == "__main__":
    MiniMenuApp().run()
