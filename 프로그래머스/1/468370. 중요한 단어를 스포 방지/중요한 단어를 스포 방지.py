def solution(message, spoiler_ranges):
    answer = 0
    splited_message=message.split()
    li=[-1]*(len(message))
    d={}
    idx=0
    spoiler_word=set()
    check=0 # 0=이전에0, 1=이전에문자, 
    for i,j in enumerate(message):
        print(i,j)
        if j!=' ':
            li[i]=idx
            check=1
        #elif check and j!=' ':
        elif check and j==' ':
            check=0
            idx+=1
    #for i in range(len(splited_message)):
    #    print(splited_message[i],idx,idx+len(splited_message[i]))
    #    for j in range(idx,idx+len(splited_message[i])):
    #        li[j]=i
    #    idx+=1+len(splited_message[i])
    print(li)
    for x,y in spoiler_ranges:
        for i in range(x,y+1):
            if li[i]!=-1:
                spoiler_word.add(li[i])
    for i in range(len(message)):
        if li[i]!=-1 and li[i] not in spoiler_word:
            d[splited_message[li[i]]]=1
    for i in sorted(list(spoiler_word)):
        if splited_message[i] not in d:
            answer+=1
            d[splited_message[i]]=1
    print(d)
    print(li)
    print(spoiler_word)
    return answer