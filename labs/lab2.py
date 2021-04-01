from random import randint
from time import sleep
print("welcom to are game!!\neach tourn cost 3nis")
sleep(1)
money=int(input("enter how many do u have:"))
sleep(2)
turnes=(money//3)
price=0
sleep(1)
print("------------")
print("you can play :" + str(turnes//3)+ " games\nyour change is :" + str(money%3))
for i in range(turnes):
    print("round number :" +str(i+1)+"\n")
    cube1=randint(1,6)
    cube2=randint(1,6)
    if(cube1==cube2):
        if(cube1=="6"):
            price=price+1000
        else:
            price=price+100
    elif(cube1=="1"):
        price=price+40
    else:
        price=price+20
print("your price is : \n" + str(price))



























