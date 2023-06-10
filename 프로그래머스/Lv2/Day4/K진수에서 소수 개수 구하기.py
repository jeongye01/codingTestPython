#https://school.programmers.co.kr/learn/courses/30/lessons/92335
##내 풀이->테스트 통과 DATE=>6.10 풀이시간 60분 
from collections import deque

def checkPrime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def solution(n, k):
    answer=0
    trans=deque()
    while n > 0:
        trans.appendleft(n % k)
        n //= k
    trans+=[0]
    tmp=""
    print(trans)
    for t in trans:
        if t==0 and tmp:
            if checkPrime(int(tmp)):
                print(tmp)
                answer += 1
            tmp = ""
        else:
            tmp += str(t)

    return answer