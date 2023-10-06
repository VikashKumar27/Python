class employee1:
    def store_details(self,name , dept, email,age):
        self.name = name
        self.dept = dept
        self.email = email
        self.age = age
    def display(self):
        print(self.name+" "+self.dept+" "+self.email+" "+str(self.age))
print("Main function starts..")
for i in range(1):
    e1 = employee1()
    name  = input("Enter name : ")
    dept  = input("Enter dept : ")
    email  = input("Enter email : ")
    age  = input("Enter age : ")
    e1.store_details(name,dept,email,age)
    e1.display()
    



