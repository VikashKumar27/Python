class person(object):
    
    def speak(self):
        print("Speaking....")
    def eating(self):
        print("Eating....")

    
class school(person):
    def details(self,name,age):
        self.name = name
        self.age = age
        return self.name , self.age

student = school()
var1= student.details("Vikash",23)
print(var1)
print(student.speak())
print(student.eating())