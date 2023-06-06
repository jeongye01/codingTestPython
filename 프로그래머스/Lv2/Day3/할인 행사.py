#https://school.programmers.co.kr/learn/courses/30/lessons/131127
#내 풀이->테스트 통과 DATE=>6.5 풀이시간 17분 
def solution(want, number, discount):
    answer = 0
    wd = {}
    for i,w in enumerate(want):
        wd[w]=number[i]
    for i in range(len(discount)):
        answer+=1
        for w in want:
            if discount[i:i+10].count(w)<wd[w]:
                answer-=1
                break

    return answer