N=int(input())
fi=[0,1,1,2,3,5,8]
for i in range(5,7998):
    fi.append(fi[-1]+fi[-2])
print(fi[2*N-1]*N%100007)