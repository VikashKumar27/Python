list1 = [100,1,2,3,4,5]
list1.sort()
print(list1)

list1 = [100,1,2,3,4,5]
list1.sort(reverse=True)
print(list1)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana","Apple" ,"Cat"]
thislist.sort()
print(thislist)

# string is a sequence of characters
#strings comes unders doubles quotes
# some functions of strings like - lstrip() , rstrip() , len , sort

thislist = ["orange", "mango", "kiwi", "pineapple", "banana","Apple" ,"Cat","z-index","xyz","yx"]
thislist.sort(reverse= True)
print(thislist)

list2 = [1,2,3,4]
print(max(list2))

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist[::-1])

thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist[-1:])

string = "Banana"
print(string[::-1])
print(string[0])

thislist = ["banana", "Orange", "Kiwi", "cherry"]
newlist = [item[::-1] for item in thislist]
print(newlist)



