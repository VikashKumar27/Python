my_list = [1,2,3,4,5,6,7,8,9,10]
even_list = []
odd_list = []
for item in my_list:
    if item % 2 == 0:
        even_list.append(item)
    else:
        odd_list.append(item)

print("Even list is : ",even_list)
print("odd list is : ",odd_list)
