#두 개의 숫자열
#내 풀이->테스트 통과 DATE=>5.3 풀이시간 5분 
T = int(input())

for test_case in range(1, T + 1):
  n,m=map(int,input().split())
  short=list(map(int,input().split()))
  long=list(map(int,input().split()))
  ans=-1e9
  if(n>m):
    short,long=long,short
    n,m=m,n
  for i in range(m-n+1):
    tmp=0
    for j in range(n):
      tmp+=short[j]*long[i+j]
    ans=max(ans,tmp)
      
  
    
      
      
  print(f"#{test_case}", ans) 