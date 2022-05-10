num=int(input("enter a number "))
i=2
count=0
while i<=num//2:
    if i%num==0:
        count+=1
        break
    i+=1
if count==0 and num!=1:
    print("its a prime number: ")
else:
    print("not a prime number: ")