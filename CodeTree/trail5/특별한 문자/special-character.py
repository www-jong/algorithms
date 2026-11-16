str = input()
d={}
for i,j in enumerate(str):
    if j in d:
        d[j]=[d[j][0]+1,i]
    else:
        d[j]=[1,i]
r=[100001,'']
for k,v in d.items():
    cnt,idx=v
    if cnt==1 and (r[0]==100001 or idx<r[0]):
        r=[idx,k]

print('None' if r[0]==100001 else r[1])