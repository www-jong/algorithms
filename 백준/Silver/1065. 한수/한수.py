count=0
for i in range(1,1+int(input())):
    if i<100:
        count+=1
    else:
        arr=list(map(int,str(i)))
        check=1
        for j in range(len(arr)-2):
            if (arr[j+1]-arr[j])!=(arr[j+2]-arr[j+1]):
                check=0
                break
        if check==1:count+=1
print(count)
        