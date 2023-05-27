
#https://school.programmers.co.kr/learn/courses/30/lessons/176963
#내 풀이->테스트 통과 DATE=>5.27 풀이시간 5분 
def solution(name, yearning, photo):
    answer = []
    d=dict()
    for i in range(len(name)):
        d[name[i]]=yearning[i]
    for p in photo:
        point=0
        for n in p:
            if n in d:
                point+=d[n]
        answer.append(point)
    return answer