
T = int(input())

for tc in range(1, T + 1):
  n,r=map(int,input().split())
  d=[0]*(n+1)
  # n 팩토리얼까지 구하기
  d[1]=1
  for i in range(2,n+1):
    d[i]=(d[i-1]*i)%1234567891
  
  print(d[n],d[r],d[n-r])
  ans=int(d[n]/(d[r]*d[n-r]))

  
  print(f"#{tc} {ans}")