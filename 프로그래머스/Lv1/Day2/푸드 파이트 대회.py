# https://school.programmers.co.kr/learn/courses/30/lessons/134240
#내 풀이->테스트 통과 DATE=>5.28 풀이시간 7분 
def solution(food):
    answer = ''
    for i,f in enumerate(food):
       answer+=str(i)*(f//2)    
    return answer+"0"+answer[::-1]