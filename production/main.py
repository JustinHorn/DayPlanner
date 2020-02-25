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

import sys
import os
#sys.path.append(os.path.join("./production/logic"))
#sys.path.append(os.path.join("./production/manager"))

from logic.plan import Plan
from logic.routine import Routine
from logic.entry import Entry
from logic import ParseText

from manager.fileManager import FileManager
from manager.timeManager import TimeManager
from manager.planManager import PlanManager
from manager.functionManager import FunctionManager
from popmenu import PopMenu

class DayPlannerGUI(Widget):

    b_save = ObjectProperty()
    b_load = ObjectProperty()
    rv_temp = ObjectProperty()
    t_plan = ObjectProperty()
    rv_entries = ObjectProperty()
    b_mode= ObjectProperty()
    t_theme= ObjectProperty()

    plan_manager = None
    file_manager = None
    func_manager = None
    time_manager = None

    def __init__(self):
        super().__init__()
       
        self.file_manager = FileManager("material/","plans/")
        self.file_manager.loadRoutines()

        self.plan_manager = PlanManager(self.updateWidgets)
        self.time_manager = TimeManager(textinput=self.t_theme)
        self.plan_manager.addUpdateStructure(self.updateEntryListLabels)
        self.func_manager = FunctionManager(self.plan_manager)

        self.loadPlan()
        self.setRoutines()

        keyboard = Window.request_keyboard(self._keyboard_released,self)
        keyboard.bind(on_key_down = self.on_key_down)

    def updateTheme(self,text):
        if not self.plan_manager == None:
            self.plan_manager.updateTheme(text)

    def _keyboard_released(self):
        self.focus = False

    def on_key_down(self,window,keycode,text,modifiers):
        if "ctrl" in modifiers:
            char = keycode[1]
            if  not char == None:
                hotkeys = self.time_manager.getHotKeys()
                hotkeys['#']=self.updateWidgets
                hotkeys['spacebar']=self.update
                hotkeys['enter'] = self.insertTime
                hotkeys['alt-gr'] = self.markedText_toRoutine
                if self.b_mode.text == "P/R":
                    hotkeys['s']=self.savePlan
                    hotkeys['l']=self.loadPlan
                else:
                    hotkeys['s']=self.saveRoutine
                func = hotkeys.get(char) 
                if not func == None:
                    func()
        
    def markedText_toRoutine(self):
        t = Routine("new routine")
        entries = ParseText.planText_toEntries(self.t_plan.selection_text)
        t.addAll(entries)
        self.plan_manager.setRoutine(t)
        self.change()
    
    def insertTime(self):
        p = self.plan_manager.plan
        t = self.t_plan.text
        i = self.t_plan.cursor_row

        entry_index = ParseText.getEntryNumber_beforeLine(t,i) -1
        entry = self.plan_manager.plan.getEntryAtIndex(entry_index)
        self.t_plan.insert_text(entry.getEnd()+" ")
  
    def savePlan(self):
        self.file_manager.savePlan(self.plan_manager.plan)
    
    def setRoutines(self):
        self.rv_temp.data = []
        for routine in self.file_manager.routines:
                self.rv_temp.data.append({'text': routine.getThemeDuration(),
                "on_press": self.func_manager.getAddTemp(routine)})

    def loadPlan(self):
        name = self.t_theme.text
        plan = self.file_manager.loadPlan(name)
        if not plan == None:
            self.plan_manager.setPlan(plan)
        
    def saveRoutine(self):
        self.file_manager.saveRoutine(self.plan_manager.routine)  

    def changeMode(self):
        self.plan_manager.swapActive()
        self.change()
        self.updateWidgets()
    
    def update(self):
        self.plan_manager.updateText(self.t_plan.text)

    def updateWidgets(self):
        self.t_theme.text = self.plan_manager.active.theme
        self.t_plan.text = self.plan_manager.active.getText()
        self.updateEntryListLabels()

    def change(self):
        if self.b_mode.text == "P/R":
            self.b_mode.text = "R/P"
            self.b_load.opacity = 0
            self.b_save.text="save routine"
            self.t_theme.text = self.plan_manager.getTheme()
            self.b_save.on_press = self.saveRoutine
        else:
            self.setRoutines()
            self.b_mode.text = "P/R"
            self.b_load.opacity = 1
            self.b_save.text="save plan"
            self.b_save.on_press = self.savePlan
            self.t_theme.text = self.plan_manager.getTheme()

    def updateEntryListLabels(self,index=0):
        self.rv_entries.data = self.rv_entries.data[:index]
        for e in self.plan_manager.active.step_list[index:]:
            self._appendEOT(e)
      
    def _appendEOT(self,eOT:Entry):
        index = len(self.rv_entries.data)
        f_m = self.func_manager
        func = f_m._getShow_popMenu if isinstance(eOT,Routine) else f_m._getRemoveEntry
        if isinstance(self.plan_manager.active,Plan):
            dic = {'text': eOT.getStartThemeDuration(),"on_press": func(index)}
        else:
            dic = {'text': eOT.getThemeDuration(),"on_press": func(index)}
        self.rv_entries.data.append(dic)

class MainGUIApp(App):

    def build(self):
        self.title = "DayPlanner"
        return DayPlannerGUI()

if __name__ == '__main__':
    MainGUIApp().run()