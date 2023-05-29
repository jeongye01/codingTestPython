#https://school.programmers.co.kr/learn/courses/30/lessons/82612
##내 풀이->테스트 통과 DATE=>5.29 풀이시간 5분 
def solution(price, money, count):
    for i in range(1,count+1):
        money-=price*i
    return abs(money) if money<=0 else 0