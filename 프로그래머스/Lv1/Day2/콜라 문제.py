#https://school.programmers.co.kr/learn/courses/30/lessons/132267
##내 풀이->테스트 통과 DATE=>5.28 풀이시간 10분 
def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += (n // a) * b
        n = n - (n // a) * a + (n // a) * b
    return answer