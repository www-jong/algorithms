N,M,*L=map(int,open(0).read().split())
A,B,C,D=zip(L[::2],L[1::2])
R=range
def K(s,e,v):
 q=[(*s,0)];v[s[0]][s[1]]=1
 for x,y,c in q:
  if(x,y)==e:return c
  for i in R(4):
   X,Y=x+[0,0,1,-1][i],y+[1,-1,0,0][i]
   if 0<=X<=N and 0<=Y<=M and not v[X][Y]:v[X][Y]=x,y;q+=[(X,Y,c+1)]
 return 1e5
def f(a,b,c,d):
 v=[[0]*(M+1)for _ in R(N+1)]
 v[c[0]][c[1]]=v[d[0]][d[1]]=1
 if(l:=K(a,b,v))>9e4:return 1e5
 V=[[0]*(M+1)for _ in R(N+1)];x,y=b
 while 1:
  V[x][y]=1
  if(x,y)==a:break
  x,y=v[x][y]
 return l+K(c,d,V)
a,b=f(A,B,C,D),f(C,D,A,B)
r=min(a,b)
print(r if r<1e5 else"IMPOSSIBLE")