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

    entry_list = ObjectProperty() 
    b_delete = ObjectProperty()

    def __init__(self,template:Template,delete_press=None,get_splitFunc=None):
        super().__init__()
        for i,e in enumerate(template.step_list):
            if i == 0:
                self.addToEntryList(i,e)
            else:
                self.addToEntryList(i,e,get_splitFunc=get_splitFunc)

        self.b_delete.on_press = delete_press

    def addToEntryList(self,index, entry,get_splitFunc=None):
        if not get_splitFunc == None:
            self.addSplitButtonToEntryList(index,get_splitFunc)

        self.entry_list.data.append({"text":str(index)+" "+entry.toString()
        })
   

    def addSplitButtonToEntryList(self,split_point,get_splitFunc):
        self.entry_list.data.append({"text":"split",
        "on_press":get_splitFunc(split_point)})

class PopMenuApp(App):
    def build(self):
        t = Template("Template_Theme")
        t.add(Entry("00:00","test_entry_theme")) 
        return PopMenu(t)

if __name__ == "__main__":
    PopMenuApp().run()
