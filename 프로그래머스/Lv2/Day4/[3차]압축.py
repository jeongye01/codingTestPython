#https://school.programmers.co.kr/learn/courses/30/lessons/17684
##내 풀이->테스트 통과 DATE=>6.10 풀이시간 100분 
from collections import deque
def solution(msg):
    q = deque()
    wd = {chr(i): i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
    i=0
    while True:
        j=1
        while msg[i:j+i] in wd and j+i<=len(msg):
            j+=1
        if msg[i:j+i-1]:
            q.append(wd[msg[i:j+i-1]])
        elif i<len(msg):
            q.append(wd[msg[i]])
        wd[msg[i:j + i]]=len(wd)+1
        if i>=len(msg)-1:
            break
        i = j + i - 1
    #print(wd)
    return list(q)