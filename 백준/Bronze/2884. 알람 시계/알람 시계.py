a,b=input().split()
a=int(a)
b=int(b)
if (a*60+b)>=45:c=a*60+b-45
else: c=a*60+b+1395
print("%d %d"%(c/60,c%60))

