#https://school.programmers.co.kr/learn/courses/30/lessons/12947
#내 풀이->테스트 통과 DATE=>6.1 풀이시간 1분 
def solution(x):
    return x%sum(list(map(int,str(x))))==0