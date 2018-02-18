class Bot:

    def __init__(self):
        self.triggers = []
        self.urls = []
        self.messages = []
        self.texts_list = []
        
    def add_trigger(self, trigger):
        self.triggers += trigger

    def showTriggers(self):
        for trigger in triggers:
            print str(trigger)
        
    def delTrigger(self, trigger):
        self.triggers.remove(trigger)
        
    def 

class Trigger:
    def __init__(self):
        self.criteria = []
        
    def addCriteria(self, criteria):
        self.criteria += criteria

    def showCriteria(self):
        for criterium in criteria:
            print str(criterium)
        
    def delCriteria(self, criteria):
        self.criteria.remove(criteria)