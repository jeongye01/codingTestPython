#https://velog.io/@wodnr0710/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV.2-%EC%97%B0%EC%86%8D%EB%90%9C-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9
from collections import deque


def solution(sequence, k):
    answer = []
    sequence += [0]

    q = deque()
    sum = 0
    start, end = 0, 0
    result = len(sequence)
    for i in range(len(sequence)):
        while sum > k:
            temp = q.popleft()
            sum -= temp
            start += 1
        if sum == k and end - start < result:
            answer = [start, end]
            result = end - start

        q.append(sequence[i])
        sum += sequence[i]
        end = i

    return answer

#투포인터
'''

def solution(sequence, k):
    n = len(sequence)

    max_sum = 0
    end = 0
    interval = n

    for start in range(n):
        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1
        if max_sum == k and end-1-start < interval:
            res = [start, end-1]
            interval = end-1-start
        max_sum -= sequence[start]

    return res

'''