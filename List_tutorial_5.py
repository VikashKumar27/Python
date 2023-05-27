my_list = [1,2,3,4,5,6,7,8,9,10]
even_list = []
odd_list = []
for item in my_list:
    if item % 2 == 0:
        even_list.append(item)
    else:
        odd_list.append(item)

even_mul = 1
for elements in even_list:
    even_mul = even_mul*elements
print(even_mul)


even_power = []
for elements in even_list:
    # power1 = pow(elements,2)
    power1 = elements**2
    even_power.append(power1)
print("Even Power list : ",even_power)

    



odd_mul = 1
for elements in odd_list:
    odd_mul = odd_mul*elements
print(odd_mul)




