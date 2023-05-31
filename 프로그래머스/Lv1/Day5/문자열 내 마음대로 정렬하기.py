#https://school.programmers.co.kr/learn/courses/30/lessons/12915
###내 풀이->테스트 통과 DATE=>6.1 풀이시간 10분 
def solution(strings, n):
    arr=[str(i) for i in strings]
    arr.sort()
    arr.sort(key=lambda x:x[n] )
    ans=[]
    for a in arr:
        ans.append("".join(a))
    return ans