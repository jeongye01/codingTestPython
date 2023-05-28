#https://school.programmers.co.kr/learn/courses/30/lessons/135808
##내 풀이->테스트 통과 DATE=>5.27 풀이시간 8분 
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0, (len(score) // m) * m, m):
        answer += min(score[i:i+m]) * m
    return answer