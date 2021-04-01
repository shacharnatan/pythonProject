from time import sleep
print("now we get the deatlis about u and your friends !!\n--------------")
for i in range(2):
    name=input("enter your name :")
    age=int(input("enter your age:"))
    phone=int(input("enter your phone:"))
    print("this is the data about studnet number:" +str(i) +"\n----------")
    sleep(2)
    print("full name is :" + name +"\nyour age is:" + str(age) +"\nyour phone is :" + str(phone))

print("----------\nbye bye")
