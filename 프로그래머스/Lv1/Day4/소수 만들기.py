#https://school.programmers.co.kr/learn/courses/30/lessons/12977
###내 풀이->테스트 통과 DATE=>6.1 풀이시간 5분 
from itertools import combinations
def solution(nums):
    answer = 0
    for comb in list(combinations(nums,3)):
        s=sum(comb)
        isPrime=1
        for i in range(2,int(s**0.5)+1):
            if s%i==0:
                isPrime=0
                break
        answer+=isPrime

    return answer