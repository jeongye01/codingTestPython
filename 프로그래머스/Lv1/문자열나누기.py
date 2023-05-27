#https://school.programmers.co.kr/learn/courses/30/lessons/140108/solution_groups?language=python3
#내 풀이->테스트 통과 DATE=>5.27 풀이시간 10분 
def solution(s):
    answer = 0
    flag=""
    cnt=0
    for x in s:
        if flag=="":
            flag=x
            cnt=1
            continue
        cnt+=(1 if x==flag else -1)
        if cnt==0:
            answer+=1
            flag=""
    if flag:
        answer+=1
        
    return answer