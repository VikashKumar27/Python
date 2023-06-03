# age  = int(input("Enter the you age : "))
# if age>=18:
#     print("Eligible for drive")
# else:
#     print("Not eligible")

# age  = int(input("Enter the age : "))
# if 18 <= age <= 22:
#     print("Eligible")
# else:
#     print("Not eligible")

# age = int(input("Enter the first no : "))
# if age > 18:
#     print("yes")

age = int(input("Enter the age : "))
while True:
    if 50<=age<=80:
        print("old age")
        break
    elif 40<=age<=50:
        print("Profession age")
        break
    elif 30<=age<=35:
        print("Marraige age")
        break
    elif 21<=age<=29:
        print("Education age")
        break
    else:
        print("Not Matching condition....")
        break