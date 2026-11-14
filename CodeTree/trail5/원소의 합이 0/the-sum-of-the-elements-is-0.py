n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
d1={}
d2={}
res=0
for i in range(n):
    for j in range(n):
        a = A[i] + B[j]
        b = C[i] + D[j]

        d1[a] = d1.get(a, 0) + 1
        d2[b] = d2.get(b, 0) + 1

for k,v in d1.items():
    if -k in d2:
        res+=v*d2[-k]
print(res)