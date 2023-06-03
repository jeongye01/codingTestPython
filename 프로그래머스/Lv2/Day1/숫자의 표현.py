#https://school.programmers.co.kr/learn/courses/30/lessons/12924
#내 풀이->테스트 통과 DATE=>6.3 풀이시간 10분 
from collections import deque
def solution(n):
    answer = 0
    nums = [i for i in range(1, n + 1)]
    nums += [0]
    q = deque()
    sum = 0
    for i in range(1, n + 2):
        while sum > n:
            tmp=q.popleft()
            sum-=tmp
        if sum == n:
            answer += 1
        q.append(i)
        sum += i

    return answer