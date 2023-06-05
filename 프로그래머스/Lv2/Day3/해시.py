#https://school.programmers.co.kr/learn/courses/30/lessons/42578
#내 풀이->테스트 통과 DATE=>6.5 풀이시간 10분 
def solution(clothes):
    cd={}
    answer=1
    for c in clothes:
        if c[1] in cd:
            cd[c[1]]+=1
        else:
            cd[c[1]]=1
    for c in cd.values():
        answer*=(c+1)
    return answer-1