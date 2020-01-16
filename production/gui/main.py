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

    def savePlan(self,path,name):
        load.save(path+"\\"+name,self.plan_structure.plan_t.text)


    def saveTemplate(self,name):
        load.save("material\\"+name+".txt",self.plan_structure.plan_t.text)

    def loadPlan(self,path):
        self.plan_structure.plan_t.text = load.loadPlan(path)

    def createPopup(self,title,kind:int):
        a = [self.savePlan,self.saveTemplate,self.loadPlan]
        pM = PopButtons(kind,a[kind])
        pW = Popup(title=title,content=pM,size_hint=(0.8,0.8))

        pW.open()


class PopButtons(FloatLayout):

    location_grid = ObjectProperty()
    location_text = ObjectProperty()
    name_grid = ObjectProperty()
    name_text = ObjectProperty()
    b_submit = ObjectProperty()

    def __init__(self,kind,function):
        super().__init__()
        if kind == 2:
            self.name_grid.disabled=True
            self.name_grid.opacity = 0
        if kind == 1:
            self.location_grid.disabled = True
            self.location_grid.opacity = 0
        self.set_submit(kind,function)

    def set_submit(self,k,f):
        if k == 0:
            self.b_submit.on_press = self.get_k0(f)
        elif k==1:
            self.b_submit.on_press = self.get_k1(f)            
        else:
            self.b_submit.on_press = self.get_k2(f)


    def get_k0(self,f):
        def func():
            f(self.location_text.text,self.name_text.text)
        return func

    def get_k1(self,f):
        def func():
            f(self.name_text.text)
        return func

    def get_k2(self,f):
        def func():
            f(self.location_text.text)
        return func





class MainGUIApp(App):

    def build(self):
        return GUIGame()


if __name__ == '__main__':
    MainGUIApp().run()