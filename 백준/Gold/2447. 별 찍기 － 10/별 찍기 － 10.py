n=int(input())
arr=[["0"]*n for i in range(n)]
arr[0]="***"
arr[1]="* *"
arr[2]="***"
emp=" "
check_n=n
co=0
while True:
    check_n/=3
    co+=1
    if check_n==1:
        break
for i in range(1,co):
    emp=emp*3
    for j in range(3**i,(3**i)*2):
        arr[j]=arr[j-3**i]+emp+arr[j-3**i]
    for j in range(0,3**i):
        arr[j]=arr[j]*3
    for j in range((3**i)*2,(3**i)*3):        
        arr[j]=arr[j-(3**i)*2]
if n==3:
    for i in range(3):
        print(arr[i])
else:
    for i in range(n):
        print(arr[i])

    