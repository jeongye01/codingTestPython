#https://school.programmers.co.kr/learn/courses/30/lessons/42839
###내 풀이->테스트 통과 DATE=>6.20 풀이시간 5분 
from itertools import permutations
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def solution(numbers):
    numbers=list(map(str,numbers))
    length=len(numbers)
    ps=set()
    for i in range(1,length+1):
        for perm in list(permutations(numbers,i)):
            if isPrime(int(''.join(list(perm)))):
                ps.add(int(''.join(list(perm))))
    return len(ps)