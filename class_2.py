class school:
    name = "Vikash"
    

    def display(self,name,age):
        self.name = name
        self.age = age
        return self.name , self.age
    
student = school()
var1= student.display("Vikash",21)
print("My name is Vikash : ",var1)