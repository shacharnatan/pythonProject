def market() :
    print("lets do a shooping! \nthis are menu:\ncola:10\nsoda:5\nbanna:15\nchiken:20")
    cola=int(input("enter how many cola u want?"))
    soda=int(input("enter how many soda u want?"))
    banna=int(input("enter how many banna u want?"))
    chiken=int(input("enter how many chiken u want?"))
    import time
    time.sleep(2)
    print("--------------")
    sumary=(cola*10)+(soda*5)+(banna*15)+(chiken*20)
    chake=input("are u done?")
    if(chake=="yes" or chake=="i want" or chake=="lets do it"):
        print("your chake with no tax is :" + str(sumary))
    else:
        print(input("do u like to cotinue with shooping?"))
    chake1="yes"
    if(chake1=="yes" or chake1=="i want" or chake1=="lets do it"):
        print(input("-----------\nenter how many cola u want? \nenter how many banna u want?\nenter how many soda u want?\nenter how many chiken u want?"))
    else:
        print("u have to choose to cotinue!")
for i in range(10):
    market()





#print("your chake with  tax is :" +str(sumary*1.17))
