#https://school.programmers.co.kr/learn/courses/30/lessons/131705
# ##내 풀이->테스트 통과 DATE=>5.28 풀이시간 5분 
from itertools import combinations
def solution(number):
    answer = 0
    for c in list(combinations(number,3)):
        if sum(c)==0:
            answer+=1
    return answer