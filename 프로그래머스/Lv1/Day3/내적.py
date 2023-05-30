#https://school.programmers.co.kr/learn/courses/30/lessons/70128
###내 풀이->테스트 통과 DATE=>5.29 풀이시간 1분 
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer+=a[i]*b[i]
    return answer