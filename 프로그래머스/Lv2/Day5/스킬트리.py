#https://school.programmers.co.kr/learn/courses/30/lessons/49993
#내 풀이->테스트 통과 DATE=>6.14 풀이시간 15분 
def solution(skill, skill_trees):
    answer = 0
    sd={key:i for i,key in enumerate(skill)}
    for s in skill_trees:
        o=0
        answer+=1
        for x in s:
            if x in sd:
                if o!=sd[x]:
                    answer-=1
                    break
                o+=1
    return answer