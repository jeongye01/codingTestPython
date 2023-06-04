#https://school.programmers.co.kr/learn/courses/30/lessons/12914
##내 풀이->테스트 통과 DATE=>6.4 풀이시간 30분 
def solution(n):
    dp=[0]*2001
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-2]+dp[i-1]
    return dp[n]%1234567