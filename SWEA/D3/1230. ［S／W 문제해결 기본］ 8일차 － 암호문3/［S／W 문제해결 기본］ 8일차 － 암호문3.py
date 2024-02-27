i,I=input,int
for t in range(10):
 n,c,s,o=I(i()),i().split(),I(i()),i().split()[::-1]
 while o:
  w,x=o.pop(),I(o.pop())
  if w=='I':y=I(o.pop());c=c[:x]+[o.pop()for _ in range(y)]+c[x:]
  if w=='D':c=c[:x]+c[x+I(o.pop()):]
  if w=='A':c+=[o.pop()for _ in range(x)]
 print(f'#{t+1}',*c[:10])