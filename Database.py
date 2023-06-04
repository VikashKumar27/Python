import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "1234")  
  
#printing the connection object   
mycursor = myconn.cursor()

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
