#https://school.programmers.co.kr/learn/courses/30/lessons/68644
#내 풀이->테스트 통과 DATE=>5.29 풀이시간 5분 
from itertools import combinations
def solution(numbers):
    answer = set()
    for comb in combinations(numbers,2):
        answer.add(sum(comb))
    return sorted(answer)