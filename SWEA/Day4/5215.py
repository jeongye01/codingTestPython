#햄버거 다이어트
#내 풀이->테스트 통과 DATE=>5.5 풀이시간 60분 
def bt(i,tt,tc):
  global ans
  if(i==n or tc+array[i][1]>m):
    ans=max(ans,tt)
    return

  bt(i+1,tt+array[i][0],tc+array[i][1])
  bt(i+1,tt,tc)
    
    
  
T = int(input())
for tc in range(1, T + 1):
  n,m=map(int,input().split())
  array=[list(map(int,input().split())) for _ in range(n)]
  array.sort(key=lambda x:x[1])
  ans=0
  bt(0,0,0)

    

  print("#{} {}".format(tc,ans))