#https://school.programmers.co.kr/learn/courses/30/lessons/12900
#내 풀이->테스트 통과 DATE=>6.16 풀이시간 3분 
def solution(n):
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=(dp[i-1]+dp[i-2])%1000000007
    return dp[-1]