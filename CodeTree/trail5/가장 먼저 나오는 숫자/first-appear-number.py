n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))
d={}
for i in range(n):
    if arr[i] not in d:
        d[arr[i]]=i+1

for i in query:
    if i in d:
        print(d[i])
    else:
        print(-1)