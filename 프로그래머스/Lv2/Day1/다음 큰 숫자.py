#https://school.programmers.co.kr/learn/courses/30/lessons/12911
#내 풀이->테스트 통과 DATE=>6.3 풀이시간 5분 
def solution(n):
    big=n+1
    cnt=format(n,'b').count("1")
    while True:
        if cnt==format(big,'b').count("1"):
            break
        big+=1
    return big