class mother:
    def nanighar(self):
        print("I am going to my nanighar in summer holidays...")

class father:
    def properties(self):
        print("I have land properties...")

class son(mother,father):
    def engineering_details(self):
        print("I  done my engineering...")

s1  =  son()
s1.nanighar()
s1.properties()
s1.engineering_details()