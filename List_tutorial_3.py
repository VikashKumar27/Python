my_list = [1,2,3,4,5,6,7,8,9,10]
# find the old elements from the list:
odd_item = []
for item in my_list:
    if item % 2 !=0:
        odd_item.append(item)
print(odd_item)

#find the even elements from the list:
even_item = []
for item in my_list:
    if item % 2 == 0:
        even_item.append(item)
print(even_item)



