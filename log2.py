ayu=[2,3,2,34,4,4,4,4,4,4,4,4,4,4]
user=int(input("enter how many number you want to delete: "))
i=1
while i<=user:
    ayu.pop()
    i+=1
print(ayu)