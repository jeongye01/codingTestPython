#https://school.programmers.co.kr/learn/courses/30/lessons/42842
#내 풀이->테스트 통과 DATE=>6.3 풀이시간 20분 
def solution(brown, yellow):
    answer = []
    for col in range(yellow,0,-1):
        if yellow%col==0 and ((yellow//col)*2+col*2+4)==brown:
            answer=[col+2,yellow//col+2]
            break
            
    return answer