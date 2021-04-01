from time import sleep
choise=str(input("\nare menu is :\n1.put a number and *3:\n2.put 4 ips adderse:\n3.chake 4 enitres in dns:\n4.chake if a srting:\nwhat are u want to choose?:"))
while(true):
    if(choise=="1"):
        print(int(input("enter a number :")) ** 3)
    elif(choise=="2"):
        ip_list=[]
    for ip_list in range(3):
         ip_list.append(input("enter a ip:"))
         print("your list ip is :" +str(ip_list))
        elif(choise=="3"):
        dns_dict={}
        dns_dict.update({input("enter a url:"):input("enter a ip :")})
        dns_dict.update({input("enter a url:"): input("enter a ip :")})
        dns_dict.update({input("enter a url:"): input("enter a ip :")})
        dns_dict.update({input("enter a url:"): input("enter a ip :")})
        print("your dns dict is :\n------------\n" + str(dns_dict))
       elif(choise=="4"):
        word=input("enter a word:")
        if(word==word[::-1]):
        print("this is polidrom")
         else:
        print("this isnt polidrom")












