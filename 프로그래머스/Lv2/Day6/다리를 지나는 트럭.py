#https://school.programmers.co.kr/learn/courses/30/lessons/42583
##내 풀이->테스트 통과 DATE=>6.20 풀이시간 30분 
from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights=deque(truck_weights)
    time=0
    passing=deque([0]*bridge_length)
    summary=0
    while truck_weights:
        time+=1
        summary-=passing.pop()
        if truck_weights and summary+truck_weights[0]<=weight:
            t=truck_weights.popleft()
            summary+=t
            passing.appendleft(t)

        else:
            passing.appendleft(0)
    for i in range(len(passing)):
        if passing[i]!=0:
            return time+len(passing)-i