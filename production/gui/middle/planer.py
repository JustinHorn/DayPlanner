import kivy
kivy.require('1.11.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.recycleview import RecycleView
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import sys
sys.path.append(".\\production\\logic")

from plan import Plan
from template import Template
from entry import Entry
try:
    from .pop.popmenu import PopMenu
except:
    from pop.popmenu import PopMenu

class Planer(FloatLayout):
    textinput = ObjectProperty()
    rv_b_entries = ObjectProperty()
    t_theme = ObjectProperty()
    b_mode = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plan = Plan("Heute")
        self.template = Template("Tempalte Theme")
        self.source = self.plan
        self.m = 0
        try:
            self._ini()
        except:
            pass

    
    def changeMode(self):
        self.removeAction()
        if self.m == 0:
            self.m = 1
            self.source = self.template
            self.b_mode.text = "T/P"
            
        else:
            self.m=0
            self.source = self.plan
            self.b_mode.text = "P/T"
        
        def func():self.source.theme = self.t_theme.text
        self.t_theme.bind(on_text = func)
        self.textinput.bind(on_text = self.update)    
        self.updateWidgets()

    def _ini(self):
        def func():self.source.theme = self.t_theme.text
        self.t_theme.bind(on_text = func)
        self.textinput.bind(on_text = self.update)     

    def update(self):
        self.source.update(self.textinput.text)
        self.updateEntryListLabels(0)

    def removeAction(self):
        self.textinput.on_text = None
        self.t_theme.on_text = None

    def setPlan(self,plan):
        self.plan = plan
        self.source =plan
        self.updateWidgets()

    def atOrSet(self,eOT:Entry):
        if isinstance(self.source,Plan):
            return self._add(eOT)
        else:
            self.source = eOT
            self.updateWidgets()
            self.source = self.template



    def _add(self,eOT:Entry):
        eOT = self._addToPlan(eOT)
        index = len(self.plan.step_list)
        self.updateEntryListLabels(index)
        return eOT

    def updateEntryListLabels(self,index):
        self.rv_b_entries.data = self.rv_b_entries.data[:index]
        for e in self.source.step_list[index:]:
            self._appendEOT(e)

    def _addToPlan(self,eOT):
        eOT = self.plan.add(eOT)
        self.textinput.text = self.plan.getText()
        return eOT
      
    def _appendEOT(self,eOT:Entry):
        index = len(self.rv_b_entries.data)
        func = self._getShow_popMenu if isinstance(eOT,Template) else self._getRemoveEntry
        if isinstance(self.source,Plan):
            dic = {'text': eOT.getStartThemeDuration(),"on_press": func(index)}
        else:
            dic = {'text': eOT.getThemeDuration(),"on_press": func(index)}
        self.rv_b_entries.data.append(dic)

    def get_renameTemplate(self,temp_index):
        def renameTemplate(new_name):
            self.plan.step_list[temp_index].theme = new_name
            self.updateEntryListLabels(0)
        return renameTemplate

    def _getShow_popMenu(self,index):
        def showPopMenu():
            temp= self.plan.step_list[index]
            pM = PopMenu()
            pW = Popup(title=temp.theme,content=pM,size_hint=(0.8,0.8))
            
            pM.addEntries(temp)
            pM.addDeleteFunction(self._getRemoveEntry(index,dismiss_func=pW.dismiss))
            pM.addSplitFunction(self._get_get_splitFunc(index,dismiss_func=pW.dismiss))
            pM.addRename(self.get_renameTemplate(index))

            pW.open()
        return showPopMenu

    def _getRemoveEntry(self,index,dismiss_func=None):
        def removeEntry():
            self.removeElement(index)
            if not dismiss_func==None:
                dismiss_func()
        return removeEntry

    def _get_get_splitFunc(self,template_index,dismiss_func=None):
        def get_splitFunc(entry_index):
            def splitFunc():
                self.splitTemplate(template_index,entry_index)
                if not dismiss_func== None:
                    dismiss_func()
            return splitFunc
        return get_splitFunc
            
    def splitTemplate(self,template_index,split_index):
        self.source.splitTemplate(template_index,split_index) # must be plan
        self.updateEntryListLabels(template_index)

    def removeElement(self,index):
        self.source.remove(index)
        self.textinput.text = self.source.getText()
        self.updateEntryListLabels(index)

 
    
    def template_update(self):
        self.template_update.update(self.textinput.text)
        self.updateEntryListLabels(0)

    def updateWidgets(self):
        self.t_theme.text = self.source.theme
        self.textinput.text = self.source.getText()
        self.updateEntryListLabels(0)


class PlanerApp(App):
    def build(self):
        p = Planer()
        p.size = (500,500)
        t = Template("Template_Theme")
        t.add(Entry("00:05","test_entry_theme"))
        t.add(Entry("00:05","test_entry_theme2")) 

        p._add(t)
        return p

if __name__ == "__main__":
    PlanerApp().run()