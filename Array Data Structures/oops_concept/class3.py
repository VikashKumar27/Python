class student:
    def details(self,name,age,address): # function with arguments
        self.name = name
        self.age = age
        self.address = address
        print("Name is : "+self.name)
        print("Age is : "+str(self.age))
        print("Address is : "+self.address)




print("Main function.......")
s1 = student()
s1.details("Manish",20,"Bihar")
print("***********************")

s2 = student()
s2.details("Vikash",23,"Motihari")

print("******************")
s3 = student()
s3.details("Raj",24,"Delhi")

print("*********************")
s4 = student()
s4.details("Kumar",25,"Chennai")