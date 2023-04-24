#퇴사
n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는 데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
max_value = 0
for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)


# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)



'''
#내풀이->테스트 통과 DATE:4.24 풀이시간->40분
n=int(input())
array=[]
for _ in range(n):
    array.append(list(map(int,input().split())))

length=len(array)
dp=[0]*(n+5)
for i in range(n - 1, -1, -1):
    if(array[i][0]+i>length): #퇴사 이후에 끝나는 상담
        dp[i]=dp[i+1]
    elif(array[i][0]==1): #하루만에 끝나는 상담
        dp[i]=array[i][1]+dp[i+1]
    else:
        dp[i]=max(dp[i+array[i][0]]+array[i][1],dp[i+1])

print(dp[0])

'''