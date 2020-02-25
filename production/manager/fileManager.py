import sys
import os
join = os.path.join

from logic import load
from logic import Factory

class FileManager():
    def __init__(self,routine_path,plan_path):
        self.routine_path = join(routine_path)
        self.plan_path = join(plan_path)
        try:
            os.mkdir(self.routine_path)
        except:
            print("error cant mk template dir")
        try:
            os.mkdir(self.plan_path)
        except:
            print("error cant mk plan dir")


    def loadRoutines(self):
        try:
            self.routines = load.loadRoutineDir(self.routine_path)
        except:
            self.routines = []
            try:
                os.mkdr(self.routine_path)
            except:
                print("error cant mkdr")


    def saveRoutine(self,routine):
        if self.routines == None:
            self.routines = []
        self.routines.append(routine)
        load.save(self.routine_path+"/"+routine.theme+"routine.txt",routine.getFileText())

    def savePlan(self,plan):
        load.save(self.plan_path+plan.theme+".txt",plan.getFileText())

    def loadPlan(self,name):
        path = self.plan_path+name+".txt" 
        text = load.loadText(path)
        if not text == '' :
            plan = Factory.parsePlanFromFileText(text)
            return plan
        else:
            return None
