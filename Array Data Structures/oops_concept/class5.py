# class is a blueprint
# class stores attributes and functions of object
# when class is created no memory is allocated
# object - object is the instance of class
# when object is created memory is allocated
# object can access the methods and attributes of class
# object can access the method and attributes of class by using dot operator

class employee:
    def store_details(self,name , dept, email,age):
        self.name = name
        self.dept = dept
        self.email = email
        self.age = age
    def display(self):
        print(self.name+" "+self.dept+" "+self.email+" "+str(self.age))

e1 = employee()
e1.store_details("Manish","Development","Manish@gmail.com",23)
e1.display()


