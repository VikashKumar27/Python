class student:
    #Attributes
    name = "Vikash"
    age = 23
    address = "Motihari"
    #method
    def display_details(self): # function with no arguments
        print("Name is : "+self.name)
        print("Age is : "+str(self.age))
        print("Address is : "+self.address)

s1 = student()
s1.display_details()

s2 = student()
s2.display_details()