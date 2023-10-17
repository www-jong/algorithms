n=input()
f=int(input())
for i in range(100):
    if int(n[0:-2]+str(i if i>=10 else "0"+str(i)))%f==0:
        print(i if i>=10 else "0"+str(i))
        break
    