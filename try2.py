ayu=int(input("enter how many method do you want run in list: "))
i=1
num3=[]
while i<=ayu:
    num1=input("enter which method do you want: ")
    if num1=="append":
        num=int(input("enter a number which you append in list: "))
        num3.append(num) 
        print(num3)
    elif num1=="extend":
        num=list(input("enter a number which you extend in list: "))
        num3.extend(num)
        print(num3)
    elif num1=="insert":
        num=int(input("enter a number which number do you insert in list: "))
        num4=int(input("enter a number of poistion: "))
        num3.insert(num4,num)
        print(num3)
    elif num1=="pop":
        num3.pop()
        print(num3)
    elif num1=="remove":
        num4=int(input("enter a number of poition: "))
        num3.remove(num3[num4])
        print(num3)
    elif num1=="sort":
        num3.sort()
        print(num3)
    i+=1

        