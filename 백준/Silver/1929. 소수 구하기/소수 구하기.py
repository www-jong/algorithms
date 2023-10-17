m,n=map(int,input().split())
arr=[1]*(n+1)
for i in range(2,n+1):
    if arr[i]==1:
        if i>=m:
            print(i)
        arr[i::i]=[0]*(n//i)