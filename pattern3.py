column =4
for row in range(5):
    for column in range(column+1):
        print("*",end=" ")
        
    print()
    column -= 1
