N=int(input())
li1=sorted(list(map(int,input().split())))
li2=sorted(list(map(int,input().split())))
deg1=[li1[i+1]-li1[i] for i in range(len(li1)-1)]
deg2=[li2[i+1]-li2[i] for i in range(len(li2)-1)]
deg1.append(360000+li1[0]-li1[-1])
deg2.append(360000+li2[0]-li2[-1])
word=deg1+deg1+deg1
def KMP_table(pattern):
    len_pattern=len(pattern)
    tmp_table=[0]*len_pattern

    p_idx=0
    for idx in range(1,len_pattern):
        while p_idx>0 and pattern[idx]!=pattern[p_idx]:
            p_idx=tmp_table[p_idx-1]

        if pattern[idx]==pattern[p_idx]:
            p_idx+=1
            tmp_table[idx]=p_idx
    return tmp_table

def KMP(word, pattern):
    table=KMP_table(pattern)

    res=[]
    p_idx=0

    for idx in range(len(word)):
        # 단어와 패턴이 일치하지 않으면, p_idx를 table를 이용해 값 변경
        while p_idx>0 and word[idx]!=pattern[p_idx]:
            p_idx=table[p_idx-1]

        # 해당 idx에서 값이 일치하면 p_idx+=1
        # 만약, p_idx가 끝까지 도달했다면, 시작 인덱스값을 계산해 추가후 p_idx를 table를 이용해 값 변경
        if word[idx]==pattern[p_idx]:
            if p_idx==len(pattern)-1:
                res.append(idx-len(pattern)+2)
                p_idx=table[p_idx]
            else:
                p_idx+=1
    return res
print('possible'if KMP(word,deg2) else'impossible')