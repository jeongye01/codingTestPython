#원 안의 점
#내 풀이->테스트 통과 DATE=>5.17 풀이시간 20분 
T=int(input())
for tc in range(1,T+1):
  n=int(input())
  ans=0
  for i in range(-1*n,n+1):
    for j in range(-1*n,n+1):
      if (i*i+j*j)<=n*n:
        ans+=1
  
  print(f'#{tc} {ans}')