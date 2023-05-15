#최장 공통 부분 수열
#이미 풀었던 LCS
T=int(input())
for tc in range(1,T+1):
    s1,s2=input().split()
    n1=len(s1)
    n2=len(s2)
    #print(s1,s2)
    dp=[[0]*n1 for _ in range(n2)]
    for i in range(n2):
        for j in range(n1):
            if s1[j]==s2[i]:
                if 0<=i-1<n2 and 0<=j-1<n1:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] =  1

            else:
                if dp[i-1][j]>dp[i][j-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i][j-1]
    print(f"#{tc} {dp[-1][-1]}")