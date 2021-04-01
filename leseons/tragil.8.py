from time import sleep
print("welcome!!\nthis is are menu:")
sleep(1)
print("\n1.inster a number and *4\n2.instert a 4 ips\n3.instret a 4 dns dictoinary\n4.instret a word and chake if polidrom")
sleep(1)
while("true"=="true"):
    choise=str(input("enter what u want 1-4?: "))
    if(choise=="1"):
        sleep(1)
        print("nice choise")
        sleep(1)
        number=int(input("enter a number:"))
        sleep(1)
        print("your number *3 is :" + str(number*3))

    elif(choise=="2"):
        sleep(1)
        print("nice choise")
        sleep(1)
        ip_list=[]
        ip_list.append(input("enter a ip adraess:"))
        ip_list.append(input("enter a ip adraess:"))
        ip_list.append(input("enter a ip adraess:"))
        ip_list.append(input("enter a ip adraess:"))
        sleep(1)
        print("your list is :" + str(ip_list))

    elif(choise=="3"):
        sleep(1)
        mydict={}
        mydict.update ({input("enter a web :"):input("enter a ip :")})
        mydict.update({input("enter a web :"): input("enter a ip :")})
        mydict.update({input("enter a web :"): input("enter a ip :")})
        mydict.update({input("enter a web :"): input("enter a ip :")})
        sleep(1)
        print("your dictoinary is :" + str(mydict))

    elif(choise=="4"):
        sleep(1)
        word=input("enter a word :")
        if(word==word[::-1]):
         sleep(1)
        print("this is a polidrom!")
    else:
         sleep(1)
         print("this isnt a polidrom!")



    exit=input("do u want to quit ? yes or no")
    if(exit=="yes"):
        sleep(1)
        print("bye bye")
        break

    else:
        sleep(1)
        print("welcome back !")















