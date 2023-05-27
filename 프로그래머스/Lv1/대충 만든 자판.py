#https://school.programmers.co.kr/learn/courses/30/lessons/160586
#내 풀이->테스트 통과 DATE=>5.27 풀이시간 10분 
def solution(keymap, targets):
    answer = []
    min_touch=dict()
    for key in keymap:
        for i,k in enumerate(key):
            if k in min_touch:
                min_touch[k]=min(min_touch[k],i+1)
            else:
                min_touch[k]=i+1
    for target in targets:
        t=0
        for s in target:
            if s in min_touch:
                t+=min_touch[s]
            else:
                t=-1
                break
        answer.append(t)
                
            
    return answer