#https://school.programmers.co.kr/learn/courses/30/lessons/12982
##내 풀이->테스트 통과 DATE=>6.1 풀이시간 5분 
def solution(d, budget):
    answer = 0
    d.sort()
    idx=-1
    while idx<len(d)-1:
        idx+=1
        budget-=d[idx]
        if budget>=0:
            answer+=1
        else:
            break
    return answer