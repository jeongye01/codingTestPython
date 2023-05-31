#https://school.programmers.co.kr/learn/courses/30/lessons/12940
#내 풀이->테스트 통과 DATE=>6.1 풀이시간 1분 
import math
def solution(n, m):
    return [math.gcd(n,m),(n*m) / math.gcd(n, m),]