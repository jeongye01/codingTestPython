#https://school.programmers.co.kr/learn/courses/30/lessons/42576
#내 풀이->테스트 통과 DATE=>6.1 풀이시간 20분 
def solution(participant, completion):
    p={key:0 for key in participant}
    for i in participant:
        p[i]+=1
    for i in completion:
        p[i]-=1
    for i in participant:
        if p[i]!=0:
            return i