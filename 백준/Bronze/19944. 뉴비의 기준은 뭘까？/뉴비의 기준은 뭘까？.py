N,M=map(int,input().split())
if 1<=M<=2:
    print('NEWBIE!')
elif M<=N:
    print("OLDBIE!")
else:
    print('TLE!')