#https://school.programmers.co.kr/learn/courses/30/lessons/68935
#내 풀이->테스트 통과 DATE=>5.29 풀이시간 15분 
def solution(n):
    answer = 0
    res=[]
    while n>0:
        res.append(n % 3)
        n//=3
        print(n)
    for i,r in enumerate(reversed(res)):
        answer+=r*pow(3,i)
    return answer