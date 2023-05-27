#https://school.programmers.co.kr/learn/courses/30/lessons/147355
#내 풀이->테스트 통과 DATE=>5.27 풀이시간 5분 
def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)])<=int(p):
            answer+=1
    return answer