#https://school.programmers.co.kr/learn/courses/30/lessons/12945
#내 풀이->테스트 통과 DATE=>6.3 풀이시간 3분 

def solution(n):
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]

    return dp[-1]%1234567