#https://school.programmers.co.kr/learn/courses/30/lessons/12951
#내 풀이->테스트 통과 DATE=>6.3 풀이시간 5분 
def solution(s):
    answer = ''
    flag=True
    for x in s:
        answer += x.upper() if flag else x.lower()
        flag=True if x==' ' else False
    return answer

