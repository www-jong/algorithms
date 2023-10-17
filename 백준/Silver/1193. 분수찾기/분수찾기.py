n=int(input());a=0;i=0
while n>0:a+=1;n-=a;i+=1; 
if i%2==0:
    print("%d/%d"%((i+n),(1-n)))
else:
    print("%d/%d"%((1-n),(i+n)))