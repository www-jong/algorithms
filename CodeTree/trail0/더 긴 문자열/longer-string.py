a,b=input().split()
if len(a)<len(b):
    print(b,len(b))
elif len(a)==len(b):
    print('same')
else:
    print(a,len(a))