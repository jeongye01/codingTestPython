#https://school.programmers.co.kr/learn/courses/30/lessons/133502
#내 풀이->테스트 통과 DATE=>5.28 풀이시간 70분 
def solution(ingredient):
    answer = 0
    p = []
    for i in ingredient:
        if p and p[-1] == [1, 2, 3] and i == 1:
            answer += 1
            p.pop()
        elif p and p[-1][-1] == i - 1:
            p[-1].append(i)
        else:
            p.append([i])

    return answer