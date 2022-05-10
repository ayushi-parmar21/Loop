# num=int(input("enter any number: "))
# i=10
# while i>=1:
#     print(num*i)
#     i-=1

list=[24,67,8,3,15,9,10,13]
i=0
min=list[0]
while i<len(list):
    if min>list[i]:
        min=list[i]
    i+=1
# print(min)
j=0
min2=list[j]
while j<len(list):
    if min<list[j]:
        if min2>list[j]:
            min2=list[j]
    j+=1 
print(min2)
    