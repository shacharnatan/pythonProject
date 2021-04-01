from time import sleep
from random import randint

print("welcome to are bank this is are menu :")
sleep(2)
print("----------")
print("1.to cash 100 nls\n2.to do a list off all your friends\n3.dns dictionary off all the statsus off ypur company\n4.to chake deatelis about your dog ")
sleep(2)
while("true" == "true"):
    print("----------")
    choise=str(input("enter what u want 1-4? :"))
    print("boot.....")
    sleep(2)

    if(choise=="1"):
        code=str(input("enter your privet code :"))
        if(code==str(code*3)):
            print("boot......")
            sleep(2)
            print("this is your code !!")
            print("now we can sure that you!!")

        else:
            print("boot.....")
            sleep(2)
            print("this isnt your code !!")
    elif(choise=="2"):
        print("lets do a list off all your feinds !!")
        sleep(1)
        friends_list=[]
        for i in range(5):
            friends_list.append(input("enter name off  your friend  :"))
        print("bulidiing your friends list ....")
        sleep(2)
        list=input("do u like to see your friends list yes/no ?")
        if(list=="yes"):
            sleep(1)
            print("your friends list is : " + str(friends_list))
        elif(choise=="no"):
            print("ok lets contiune and go back to the begiing :")
            input("lets chake if your friend is in the list :")
            sleep(1)
            name=input("enter friend name :")
            if(name in friends_list):
                print("boot...")
                sleep(2)
                print(name + " is in your friends list !")




    elif(choise=="3"):
        print("lets get stared !")
        dns_dict={}
        sleep(1)
        print("now put all your data dns and i will put them in dicionary , you need to put url adrees and to put ip adrrease :")
        for i in range(4):
            sleep(1)
            dns_dict.update({input("enter a url:"):input("enter a ip :")})
        print("bulidinig your dns dicionary for your company ....")
        sleep(2)
        print("your dns dicionary is ready !")
        dns=input("do u like to see your dns dicionary yes/no?")
        if(dns=="yes"):
            sleep(1)
            print("your dns dicionary is :" + str(dns_dict))
        elif(dns=="no"):
            print("ok....")
            sleep(1)

    elif(choise=="4"):





exit=input("do u want to exit yes/no?")
if(exit=="yes"):
    print("boot....")
    sleep(1)
    print("ok , bye bye !")
    break
else:
    print("boot....")
    sleep(1)
    print("nice choise !")
    continue

