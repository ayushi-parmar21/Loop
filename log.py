ayu=[1,3,2,5,3,5,3,6,3,6,6,9,9,6,6,7,7]
i=0
count=1
while i<len(ayu):
    count+=1
    if count==5:
        ayu[i]="q"
        count=1
    i+=1
print(ayu)
    