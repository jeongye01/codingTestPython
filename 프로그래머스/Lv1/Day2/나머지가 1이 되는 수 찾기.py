#https://school.programmers.co.kr/learn/courses/30/lessons/87389
# ##내 풀이->테스트 통과 DATE=>5.28 풀이시간 5분 
def solution(n):
    answer = 0
    for i in range(2,n+1):
        if n%i==1:
            answer=i
            break
    return answer