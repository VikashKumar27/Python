class grandfather():
    def properties(self):
        print("I have 20 acree land")
class father(grandfather):
    def father_properties(self):
        print("my father have own 10 acre extra land..")
class son(father):
    pass

s1 = son()
s1.properties()
s1.father_properties()