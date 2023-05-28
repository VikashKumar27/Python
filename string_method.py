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

points = [1,1,1]
# count1 = [2,1,1,2,1,1,1]
count1 = []

for x in points:
    var1 = points.count(x)
    count1.append(var1)

print("counts of points : ",count1)









