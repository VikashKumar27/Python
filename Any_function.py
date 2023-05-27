list1 = [1,2,3,4,5]
list2 = [1,2,3,4,]
difference = []
for i in list1:
    if not any(i == j for j in list2):
        difference.append(i)
print(difference)
