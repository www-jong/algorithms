for i in range(int(input())):
    h,w,n=map(int,input().split());b=(n-1)//h;a=(n-h*(n//h));
    if a==0:a=h
    print("%d%d"%(a*10 if b+1<10 else a,b+1));
            
        