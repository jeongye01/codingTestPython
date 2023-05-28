# 덧칠하기
# https://school.programmers.co.kr/learn/courses/30/lessons/161989
#내 풀이->테스트 통과 DATE=>5.27 풀이시간 20분 
def solution(n, m, section):
    answer = 1
    left=m-1
    for i in range(1,len(section)):
        left-=(section[i]-section[i-1])
        if left<0:
            answer+=1
            left=m-1
            
        
        
    return answer