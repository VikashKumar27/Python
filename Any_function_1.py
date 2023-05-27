list1 = [["req1",1,"Released"],["req2",2,"Inwork"],["req3",3,"InWork"]]
list2 = [["req1",1,"Released"],["req2",2,"Inwork"],["req3",3,"Released"]]


difference = []
for inner_list in list1:
    if not any(inner_list == inner_list2 for inner_list2 in list2):
        difference.append(inner_list)
print(difference)



