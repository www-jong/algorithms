n,m=map(int,input().split())
ar=list(map(int,input().split()))
ar.sort()
n=len(ar)
arr=[]
while ar[n-1]<m:
    if ar[n-1]>=m:
        del ar[n-1]
    else: 
        n==0
        break
    n-=1
for a in range(len(ar)-2):
    for b in range(a+1,len(ar)-1):
        if ar[a]+ar[b]>m:
            break
        for c in range(b+1,len(ar)):
            s=ar[a]+ar[b]+ar[c]
            if s>m:
                break
            elif s<=m:
                arr.append(s)
print(max(arr))

                
    