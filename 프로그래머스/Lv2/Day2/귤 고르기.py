#https://school.programmers.co.kr/learn/courses/30/lessons/138476
#내 풀이->테스트 통과 DATE=>6.4 풀이시간 10분 
def solution(k, tangerine):
    answer = 0
    tan={}
    for t in tangerine:
        if t in tan:
            tan[t]+=1
        else:
            tan[t]=1

    tan=sorted(tan.items(), key=lambda x: x[1],reverse=True)
    cnt=0
    for t in tan:
        answer+=1
        cnt+=t[1]
        if cnt>=k:
            break
    return answer