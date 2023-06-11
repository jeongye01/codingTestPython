#https://school.programmers.co.kr/learn/courses/30/lessons/17687
##내 풀이->테스트 통과 DATE=>6.11 풀이시간 10분 
from collections import deque
def solution(n, t, m, p):
    num = 1
    play=['0']
    nd={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    while len(play) < t*m:
        trans = deque()
        tmp=num
        while tmp > 0:
            if tmp % n>=10:
                trans.appendleft(nd[tmp % n])
            else:
                trans.appendleft(str(tmp % n))
            tmp //= n
        num += 1
        play.extend(list(trans))
    play=play[0:t*m]
    return "".join([i for i in play[p-1:len(play):m]])