from random import randint
from time import sleep
while("true"):
    print("welcome to are final projacet !\nthis is are menu :\n------------\na.ip system\nb.dns system")
    sleep(1)
    choise=input("enter what u want , a or b ?")
    if(choise=="a"):
        print("this is the menu for -a: ")
        sleep(2)
        print("1.search for ip adresse from the ip list\n2.add ip adresse to a list\n3.deleat ip adersse to a list\n4.show all the ips adreese")
        n=str(input("enter what u want only 1-4 ! :"))
        ip_list = ["192.168.1.1", "198.1.1.1", "172.89.4.4", "120.34.5.3"]
        if(n=="1"):
            ip_list=["192.168.1.1","198.1.1.1","172.89.4.4","120.34.5.3"]
            ip=str(input("enter your ip that u want to serach :"))
            print("boot....")
            sleep(2)
            if(ip in ip_list):
                sleep(1)
                print(str(ip) + " is found in the ip list !")
            else:
                sleep(1)
                print("your ip is isnt found in the ip list...")
        elif(n=="2"):
            print("now u can put anduer ip adresse to the list...")
            sleep(1)
            ip_list = ["192.168.1.1", "198.1.1.1", "172.89.4.4", "120.34.5.3"]
            ip_list.append(input("enter a ip adress :"))
            print("boot....")
            sleep(2)
            print("your new ip is now in the ip list !")
            sleep(1)
            print(ip_list)
        elif(n=="3"):
            sleep(1)
            print("this is your ip list :" +str(ip_list))
            sleep(1)
            ip_list.pop(int(input("enter a ip from left 0-9 :")))
            print("boot....")
            sleep(2)
            print("the ip adersse is dealete !")
            print("the new list is :")
            sleep(1)
            print(ip_list)
        elif(n=="4"):
            sleep(1)
            print("the ip list is :\n" + str(ip_list))
        else:
            print("boot....")
            sleep(1)
            print("im sorry... only 1-4 !!")
    elif(choise=="b"):

        sleep(1)
        print("this is are menu for b :")
        sleep(2)
        print("boot....")
        print("------------")
        print("1.serach for url from dictionary\n2.add url and ip to dictionary\n3.delete url from dictionary\n4.update the ip adreese of url\n5.show all the url and ip ")
        x = int(input("enter what u want 1-5  ? :"))
        url_dict={"www.google.com" : "192.168.2.2" ,"www.ynet.com" : "194.5.5.5","www.mako.com" : "4.4.4.4"}
        if(x=="1"):
            print("now we serach your url in the dictioary :")
            sleep(1)
            y=input("enter key value :")
            if(y in url_dict):
                print("boot....")
                sleep(2)
                print("we found your url and ip")













