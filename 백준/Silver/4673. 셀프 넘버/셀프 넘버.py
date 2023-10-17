arr=[0 for i in range(0,10500)]
for i in range(1,10000):
    arr[i+sum(list(map(int,str(i))))]=1
    if arr[i]==0:
        print(i)
    
    