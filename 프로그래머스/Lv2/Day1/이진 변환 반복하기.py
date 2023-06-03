#https://school.programmers.co.kr/learn/courses/30/lessons/70129
#내 풀이->테스트 통과 DATE=>6.3 풀이시간 5분 
def solution(s):
    n = s.count("1")
    trans=1
    r=len(s)-n
    while n != 1:
        trans+=1
        tmp = ""
        while n > 0:
            tmp = str(n % 2)+tmp
            n //= 2
        n = tmp.count("1")
        r+=(len(tmp)-n)

    return [trans,r]