num=int(input("enter a number: "))
i=1
while i<=num:
    if i%2!=0:
        j=1
        while j<=5:
            if j==5:
                print(i+1,end="")
            else:
                print(i,end="")
            j+=1
        print()
    else:
        j=1
        while j<=5:
            if j==1:
                print(i+1,end="")
            else:
                print(i,end="")
            j+=1
        print()
    i+=1
            