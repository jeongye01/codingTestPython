#https://school.programmers.co.kr/learn/courses/30/lessons/42579
##내 풀이->테스트 통과 DATE=>6.28 풀이시간 20분 
def solution(genres, plays):
    gm={}
    pcm={}
    answer = []
    for i,g in enumerate(genres):
        if g in gm:
            gm[g]+=plays[i]
            pcm[g]=pcm[g]+[[plays[i],i]]
        else:
            gm[g]=plays[i]
            pcm[g] = [[plays[i], i]]
    for g in sorted(gm,key=lambda x:gm[x],reverse=True):
        tmp=pcm[g]
        tmp.sort(key=lambda x:(-x[0],x[1]))
        answer.append(tmp[0][1])
        if len(tmp)>=2:
            answer.append(tmp[1][1]
)
            

    return answer