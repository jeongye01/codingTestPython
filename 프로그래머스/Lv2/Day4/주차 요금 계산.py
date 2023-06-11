#https://school.programmers.co.kr/learn/courses/30/lessons/92341
#내 풀이->테스트 통과 DATE=>6.11 풀이시간 25분 
import math
def solution(fees, records):
    answer = []
    td={}
    for r in records:
        rl=r.split()
        if rl[1] in td:
            td[rl[1]] += [rl[0]]
        else:
            td[rl[1]] = [rl[0]]

    for n in sorted(td.keys()):
        if len(td[n])%2!=0:
            td[n].append("23:59")
        tot=0
        for k in range(0,len(td[n]),2):
            time1=td[n][k].split(":")
            time2=td[n][k+1].split(":")
            tot+=((int(time2[0])*60+int(time2[1]))-(int(time1[0])*60+int(time1[1])))
        m=fees[0]-tot
        if m>0:
            answer.append(fees[1])
        else:
            answer.append(math.ceil(abs(m)/fees[2])*fees[-1]+fees[1])




    return answer