#https://school.programmers.co.kr/learn/courses/30/lessons/87946
#내 풀이->테스트 통과 DATE=>6.5 풀이시간 5분 
from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for perm in list(permutations(dungeons,len(dungeons))):
        power=k
        cnt=0
        for p in perm:
            if power>=p[0]:
                power-=p[1]
                cnt+=1
            else:
                break
        answer=max(cnt,answer)
    return answer