# https://school.programmers.co.kr/learn/courses/30/lessons/76501
###내 풀이->테스트 통과 DATE=>5.29 풀이시간 3분 
def solution(absolutes, signs):
    answer=0
    for i,a in enumerate(absolutes):
        answer+=a if signs[i] else -1*a
    return answer