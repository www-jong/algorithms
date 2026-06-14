def solution(skill, skill_trees):
    answer = 0
    check=[0]*26
    for i in range(len(skill)):
        check[ord(skill[i])-65]=i+1
    for i in skill_trees:
        cnt=1
        for j in i:
            if check[ord(j)-65]==cnt:
                cnt+=1
            elif check[ord(j)-65]==0:
                continue
            else:
                break
        else:
            answer+=1
    return answer