#https://school.programmers.co.kr/learn/courses/30/lessons/42747
#내 풀이->테스트 통과 DATE=>6.4 풀이시간 30분 
def solution(citations):
    answer = 0
    citations.sort()
    for h in range(citations[-1]):
        u=0
        for c in citations:
            if c >= h:
                u += 1
        if u >= h:
            answer = h
    return answer