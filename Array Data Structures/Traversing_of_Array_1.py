list = []
size =  int(input("Enter the size of list : "))
for i in range(size+1):
    value = int(input("Enter the Value : "))
    list.append(value)
print(list)

pos = 2
item = 4
list.insert(2,4)
print(list)

list.append(4)
print(list)

search_item = 4
for item in range(len(list)):
    if search_item == list[item]:
        print("index of search_item is : ",item)

