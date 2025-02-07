for i in range(int(input())):
    li=list(map(int,input().split()))
    li.pop(0)
    li.sort(reverse=True)
    gap=[]
    for j in range(1,len(li)):
        gap.append(li[j-1]-li[j])
    print('Class '+str(i+1))
    print('Max '+str(max(li))+', Min '+str(min(li))+', Largest gap '+str(max(gap)))
