class school:
    
    def display(self):
        name = input("Enter the name : ")
        age = int(input("Enter the age : "))
        print("Display Details : ",name, age)

student  = school()
student.display()