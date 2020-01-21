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
from entry import Entry

class PopMenu(FloatLayout):

    entry_list = ObjectProperty() 
    b_delete = ObjectProperty()

    def __init__(self,template=None,delete_press=None,get_splitFunc=None):
        super().__init__()

    def addEntries(self,template):
        for e in template.step_list:
            self.appendEntry(e)

    def appendEntry(self, entry):
        self.entry_list.data.append({"text":entry.toString()})
   
    def addSplitFunction(self,get_splitFunc):
        l = len(self.entry_list.data)
        for i in range(l-1,0,-1):
            self.entry_list.data.insert(i,{"text":"split",
            "on_press":get_splitFunc(i)})
    
    def addDeleteFunction(self, delete_press):
        self.b_delete.on_press = delete_press

class PopMenuApp(App):
    def build(self):
        t = Template("Template_Theme")
        t.add(Entry("00:00","test_entry_theme")) 
        return PopMenu(t)

if __name__ == "__main__":
    PopMenuApp().run()
