#https://velog.io/@uoayop/BOJ-1300-K%EB%B2%88%EC%A7%B8-%EC%88%98Python
N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2
    
    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N) #mid 이하의 i의 배수 or 최대 N
    
    if temp >= K: #이분탐색 실행
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
