n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]
count={}
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for now in queries:
    if now in count:
        print(count[now])
    else:
        print(0)