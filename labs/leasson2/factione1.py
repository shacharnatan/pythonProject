def number (x,y):
    print("your first number is : " + str(x) + "\nyour secend number is : " + str(y))
    print("your new number is : " + str(x**y))
    sum=x**y
    print("your new number is :" + str(sum))
    return sum
a=int(input("enter a number :"))
b=int(input("enter a number :"))
idan=number (a,b) + 29
print("wow :" + str(idan))



