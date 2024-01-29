for i in range(int(input())):
 N=int(input())
 t,r=0,0
 while t!=1023:
  r+=N
  for j in str(r):t|=1<<(int(j))
 print(f'#{i+1}',r)
