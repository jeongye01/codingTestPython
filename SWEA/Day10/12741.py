# 두 전구
#내 풀이->테스트 통과 DATE=>5.21 풀이시간 25분 
T=int(input())
result=[]
for tc in range(1,T+1):
    data=list(map(int,input().split()))
    dp=[0]*101
    ans=0
    for i in range(data[0],data[1]+1):
        dp[i]+=1
    for i in range(data[2],data[3]+1):
        dp[i]+=1
    ans=dp.count(2)
    if ans>0:
        ans-=1
    result.append(ans)

for tc in range(1,T+1):
    print(f"#{tc} {result[tc-1]}")

#더 나은 풀이
'''
T = int(input())
lst=[]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a,b,c,d = map(int,input().split())
    ans = min(b,d)-max(a,c)
    if ans <= 0:
        ans = 0
    lst.append(ans) 
for i in range(len(lst)):
    print(f"#{i+1} {lst[i]}")
'''