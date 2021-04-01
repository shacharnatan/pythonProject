from time import sleep
from random import randint
def menu():
    while("true"):
        print("this is are menu : \n----------\n1.dogs deatiels\n2.friends list\n3.azareat")
        sleep(1)
        word=input("enter what u want ?")
        if(word=="1"):
            dogs()



        elif(word=="2"):
            friends()


        elif(word=="3"):
            azareat()


        else:
            print("enter 1-3 only!!!\n")
            continue
        exit=input("do u want to exit yes/no?")
        if(exit=="yes"):
            print("bye bye")
            break
        else:
            print("welcome back")
            continue





def dogs():
    name=input("enter dog name :")
    age=int(input("enter dog age :"))
    sleep(1)
    print("dog name : " +name +"\ndog age :" + str(age*7) +"\n------")
def friends():
    friends_list=[]
    for i in range(5):
        friends_list.append(input("enter a friend :"))

    name1=input("u like to chake if is a friend in  the list : yes/no?")
    if(name1=="yes"):
        name2=input("enter a friend name :")
        if(name2 in friends_list):
            sleep(1)
            print("your friend in the list")
        else:
            print("your friend not in the list")
    elif(name1=="no"):
        print("lets contiune")
def azareat():
    num=int(input("enter a number :"))
    sum=1
    for i in range(1,num+1):
        sum=sum*i
    sleep(1)
    print(str(num) + " azareat is :" + str(sum))



















menu()






