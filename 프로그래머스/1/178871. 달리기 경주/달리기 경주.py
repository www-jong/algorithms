def solution(players, callings):
    answer = []
    d={}
    for i in range(len(players)):
        d[players[i]]=i
    for i in callings:
        a,aname=d[i],i
        b,bname=d[players[a-1]],players[a-1]
        players[a],players[b]=players[b],players[a]
        d[aname]-=1
        d[bname]+=1
    return players