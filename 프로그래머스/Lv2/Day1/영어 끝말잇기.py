#https://school.programmers.co.kr/learn/courses/30/lessons/12981
##내 풀이->테스트 통과 DATE=>6.3 풀이시간 10분 
import math
def solution(n, words):
    answer = [0,0]
    for i in range(1,len(words)):
        if words[i] in words[0:i] or words[i-1][-1]!=words[i][0]:
           answer=[i%n+1,math.ceil((i+1)/n)] 
           break

    return answer