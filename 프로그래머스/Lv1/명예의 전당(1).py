#https://school.programmers.co.kr/learn/courses/30/lessons/138477
##내 풀이->테스트 통과 DATE=>5.27 풀이시간 10분 
def solution(k, score):
    answer = []
    for day in range(1,len(score)+1):
        answer.append(min(sorted(score[0:day])[-1*k:]))
        
    return answer