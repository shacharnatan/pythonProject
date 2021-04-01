from time import sleep
print("this is are menu:\n1.instert number and **3:\n2.instert 4 ips in a list:\n3.interst 4 dns dictionray:\n4.chake if a word is a polidrom:")

choise=str(input("enter what u want 1-4:"))
if(choise=="1"):
    x=int(input("enter a number :"))
    sleep(1)
    print("your number with **3 is :\n" + str(x**3))
elif(choise=="2"):
    ip_list=[]
    for i in range(4):
        ip_list.append(input("enter a ip:"))
    print("your  ip list is :" +str(ip_list))
elif(choise=="3"):
    my_dict={}
    my_dict.update({input("enter a web:"):input("enter a ip :")})
    my_dict.update({input("enter a web:"):input("enter a ip:")})
    my_dict.update({input("enter a web:"):input("enter a ip:")})
    my_dict.update({input("enter a web :"):input("enter a ip:")})
    sleep(1)
    print("your dictionry is :" +str(my_dict))
elif(choise=="4"):
    print("now we chake if a word is polidrom:")
    sleep(1)
    word=input("enter a word:")
if(word==word[::-1]):
        sleep(1)
        print("this is a polidrom:!")
else:
    sleep(1)
    rint("this isnt a polidrom!")



