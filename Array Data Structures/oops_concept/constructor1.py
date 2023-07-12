# constructor
# the name of constructor is same as class name
# in python constructor is init function
# when object of class is created constructor automatically called
class constructor:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name+" "+str(self.age))

c1 = constructor("Vikash",23)
c1.display()




