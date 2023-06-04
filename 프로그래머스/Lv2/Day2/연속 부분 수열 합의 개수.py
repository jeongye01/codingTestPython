#https://school.programmers.co.kr/learn/courses/30/lessons/131701
#내 풀이->테스트 통과 DATE=>6.4 풀이시간 10분 
def solution(elements):
    answer = 0
    n=len(elements)
    elements.extend(elements)
    cnt=set()
    for i in range(1,n+1):
        
        for j in range(n*2):
            cnt.add(sum(elements[j:j+i]))
    answer=len(list(cnt))
        
    return answer