a,b,c=map(int,input().split())
d=(c-b)//(a-b)
if (c-b)%(a-b)!=0:
    d+=1
print(d)
