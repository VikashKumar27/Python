import pandas as pd
# read_excel = pd.read_excel(r"C:/Users/Acer/Desktop/Student_Details.xlsx")
# print(read_excel)

data = {
    "day1":["Rice","Dal","Sabji"],
    "day2":["Chiken","Butter Nan","SoyaPanner"]

}

dataFrame = pd.DataFrame(data,index=["row1","row2","row3"])
print(dataFrame)

print("************************")

print(dataFrame.head(1))

print("****************************")
print(dataFrame.tail(1))

print("*******************************")

print(dataFrame.option.diaplay.max_row)
