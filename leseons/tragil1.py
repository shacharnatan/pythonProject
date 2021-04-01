from time import sleep
print("this are menu:\n1.instet a number and **3:\n2.instet a ip :\n3.dns dictaniory:\n4.chake if string is polidrom:\n---------")
sleep(1)
choise=input("chosee 1-4 what u want?")
if(choise=="1"):
   x=int(input("enter a number:"))
   print("your number **3 is:" +str(x**3))
elif(choise=="2"):
    iplist=[]
    iplist.append(input("enter a ip:"))
    iplist.append(input("enter a ip:"))
    iplist.append(input("enter a ip:"))
    iplist.append(input("enter a ip:"))
    sleep(1)
    print("your ip list is :" +str(iplist))
elif(choise=="3"):
    dns_dict={}
    dns_dict.update({input("enter a web :"):input("enter a ip:")})
    dns_dict.update({input("enter a web:"):input("enter a ip:")})
    dns_dict.update({input("enter a web:"):input("enter a ip:")})
    dns_dict.update({input("enter a web :"):input("enter a ip:")})
    sleep(1)
    print("your dict is :" +str(dns_dict))
elif(choise=="4"):
    word=input("enter a world:")
    if(word==word[::-1]):
        sleep(1)
        print("this is polidrom!")
else:
    print("this isnt polidrom!")




















