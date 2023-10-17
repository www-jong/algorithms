n=int(input())
p=[0,1]
if n>=2:
    for i in range(2,n+1):
        p.append(p[i-1]+p[i-2])
    print(p[n])
else:
    print(n)
