#https://school.programmers.co.kr/learn/courses/30/lessons/178871
#달리기 경주
def solution(players, callings):
    pla_dic = {key: i for i, key in enumerate(players)}
    print(pla_dic)
    for p in callings:
        c = pla_dic[p]
        pla_dic[p] -= 1
        pla_dic[players[c-1]] += 1
        players[c-1], players[c] = players[c], players[c-1]

    return players

'''
# 내풀이 시간초과
def solution(players, callings):
    d=dict()

    for i in range(len(players)):
        d[players[i]]=i

    for calling in callings:
        cd = {v: k for k, v in d.items()}
        tmp=cd.get(d[calling]-1)
        d[tmp]+=1
        d[calling]-=1
    answer=list(d.keys())
    answer.sort(key=d.get)
    return answer



'''

