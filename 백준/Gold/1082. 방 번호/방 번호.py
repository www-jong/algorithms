I=input;N=int(I());P=[*map(int,I().split())];M=int(I());d=[-1]*(M+1)
for i in range(N-1,-1,-1):
 for j in range(P[i],M+1):
  d[j]=max(d[j-P[i]]*10+i,i,d[j])
print(d[M])