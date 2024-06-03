username = "Shine Minn"
password = "8122004"

username1 = input ("Enter your username: ")
password1 = input ("Enter your password: ")

if username == username1 and password == password1:
    print ("Hello user ")
else:
    print ("invalit user")

username = "Shine Minn"
password = "8122004"

username1 = input ("Enter your name: ")
password1 = input ("Enter uour password: ")

if username == username1 and password == password1:
    print ("Hello User")
elif username != username1 and password == password1:
    print ("wrong username")
elif username == username1 and password != password1:
    print ("wrong password")
elif username != username1 and password != password1:
    print ("invalit user")
else:
    print ("system Error!")