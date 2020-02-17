import sys
import os
join = os.path.join
sys.path.append(join("./production/logic"))

import load
import Factory

class FileManager():
    def __init__(self,template_path,plan_path):
        self.template_path = join(template_path)
        self.plan_path = join(plan_path)
        try:
            os.mkdir(self.template_path)
        except:
            print("error cant mk template dir")
        try:
            os.mkdir(self.plan_path)
        except:
            print("error cant mk plan dir")


    def loadTemplates(self):
        try:
            self.templates = load.loadTemplateDir(self.template_path)
        except:
            self.templates = []
            try:
                os.mkdr(self.template_path)
            except:
                print("error cant mkdr")


    def saveTemplate(self,template):
        if self.templates == None:
            self.templates = []
        self.templates.append(template)
        load.save(self.template_path+"/"+template.theme+"template.txt",template.getFileText())

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
