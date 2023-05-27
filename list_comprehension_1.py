list1 = [1,2,3,4,5,6,7,8,9,10]
new_list_even = [item for item in list1 if item % 2 == 0]
print(new_list_even)

new_list_odd = [item for item in list1 if item % 2 != 0]
print(new_list_odd)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for item in fruits:
    if 'a' in item:
        newlist.append(item)
print(newlist)

newlist1 = [item for item in fruits if 'a' not in item ]
print(newlist1)

print([x for x in range(1,10,2)])
print([x for x in range(1,12) if x % 2 == 0])

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print([item.upper() for item in fruits])
print([item.capitalize() for item in fruits])
print([item.title() for item in fruits])
print([item.casefold() for item in fruits])


fruits = ["  apple  ", "  banana  ", "  cherry  ",  " kiwi ", " mango "]
print([item.strip()[::-1] for item in fruits])




