S=['apple','banana','grape','blueberry','orange']
s=input()
r=0
for i in S:
    if s in i[2:4]:
        print(i)
        r+=1
print(r)