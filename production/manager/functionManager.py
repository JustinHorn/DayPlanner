from kivy.uix.popup import Popup
import sys
import os
sys.path.append(os.path.join("./production/pop"))
from popmenu import PopMenu
    
class FunctionManager(): 
    def __init__(self,plan_manager):
        self.plan_manager = plan_manager

    def get_renameTemplate(self,temp_index):
        def renameTemplate(new_name):
            self.plan_manager.rename(temp_index,new_name)
        return renameTemplate

    def _getShow_popMenu(self,index):
        def showPopMenu():
            temp= self.plan_manager.active.step_list[index]
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
            self.plan_manager.removeElement(index)
            if not dismiss_func==None:
                dismiss_func()
        return removeEntry

    def _get_get_splitFunc(self,template_index,dismiss_func=None):
        def get_splitFunc(entry_index):
            def splitFunc():
                self.plan_manager.splitTemplate(template_index,entry_index)
                if not dismiss_func== None:
                    dismiss_func()
            return splitFunc
        return get_splitFunc

    def getAddTemp(self,temp):
        def addTemp():
            self.plan_manager.atOrSet(temp)
        return addTemp  