from time import sleep
from random import randint
def menu():
    while ("true"):
        print(" welcome !\nthis is are menu : \n1.dogs deatelis\n2.friends list\n3.enter a dictonary dns \n-----------")
        sleep(1)
        choise=(input("enter what u want 1-3?"))
        if(choise=="1"):
            dog()
        elif(choise=="2"):
            friend_list()
        elif(choise=="3"):
            dns_dictonary()

        else:
            print("only 1-3 !!!")
        exit=input("do u want to exit yes/no?")
        if(exit=="yes"):
            print("bye bye nice to meet u")
            break
        else:
            print("welcome back")
            continue

def dog():
    name=input("enter your dog name :")
    age=int(input("enter your dog age:"))
    print("your name dog is :" + name +"\nyour dog age in years off dog is : " +str(age*7))
def friend_list():
    friend_list=[]
    sleep(1)
    print("now you gave us 5 names of your friends :")
    print("boot.....")
    sleep(2)
    for i in range(5):
        friend_list.append(input("enter a name of your friend :"))
    print("bulidinid your friedns list....")
    sleep(3)
    print("your new list is : " +str(friend_list))
    sleep(1)
    name1=input("do u like to chake if your friend is in the list yes/no?")
    if(name1=="yes"):
        sleep(1)
        name2=input("enter a name of your friend :")
        if(name2 in friend_list):
            print("cheking...")
            sleep(1)
            print("your friend is in the list !!")
        else:
            print("cheking...")
            sleep(1)
            print("your friend is isnt in the list!")
def dns_dictonary():
    dns_dict={}
    sleep(1)
    print("now gives us a 4 url and ip adresses :")
    for i in range(4):
        sleep(2)
        dns_dict.update({input("enter a url :"):input("enter a ip :")})
    print("bulidinid your dns dict......")
    sleep(2)
    print("your dns dict is :" + str(dns_dict))




















menu()

















