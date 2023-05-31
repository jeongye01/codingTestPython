#https://school.programmers.co.kr/learn/courses/30/lessons/12948
#내 풀이->테스트 통과 DATE=>6.1 풀이시간 1분 
def solution(phone_number):
    return '*'*(len(phone_number)-4)+phone_number[-4:]