#가장 긴 감소하는 부분 수열
#https://www.acmicpc.net/problem/11722
##내 풀이->테스트 통과 DATE=>5.20 풀이시간 10분 
n=int(input())
arr=list(map(int,input().split()))
dp=[1]*n
for i in range(1,n):
    for j in range(i):
        if arr[i]<arr[j]:
            dp[i]=max(dp[j]+1,dp[i])



print(max(dp))