class car:
    def __init__(self,model_name,year): # constructor
        self.model_name = model_name
        self.year = year
    def display(self):
        print(self.model_name+"    "+str(self.year))

honda = car("honda_12",2000)
honda.display()

jlr = car("landrover",2005)
jlr.display()

