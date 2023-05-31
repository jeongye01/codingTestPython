#https://school.programmers.co.kr/learn/courses/30/lessons/12926
###내 풀이->테스트 통과 DATE=>6.1 풀이시간 1분 
def solution(s, n):
    answer = ''
    for x in s:
        if x.islower():
            answer+=chr((ord(x)-ord('a')+n)%26+ord('a'))
        elif x.isupper():
            answer+=chr((ord(x)-ord('A')+n)%26+ord('A'))
        else:
            answer+=x
    return answer