#https://school.programmers.co.kr/learn/courses/30/lessons/86491
#내 풀이->테스트 통과 DATE=>5.28 풀이시간 5분 
def solution(sizes):
    r,c=0,0
    for s in sizes:
        s.sort()
        r=max(s[0],r)
        c=max(s[1],c)
    return r*c