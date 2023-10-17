a=list(map(int,str(input())));a.sort(reverse=True);s=""
for i in range(len(a)):s+=str(a[i])
print(s)