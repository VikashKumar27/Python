list1 = ["Banana","manish","vikash"]
list2 = list1.copy()
print(list2)

str1 = ["Manish"]
str2 = ["Kumar"]
print(str1+str2)
print(str1)

fname = "Manish"
print(fname)
lname = "Kumar"
print(fname+" "+lname)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list1.extend(list2)
print(list1)

for x in list2:
    list1.append(x)

print(list1)



