#현주의 상자 바꾸기
#내 풀이->테스트 통과 DATE=>5.9 풀이시간 5분 
T = int(input())
for tc in range(1,T+1):
  n,q=map(int,input().split())
  array=[0]*n
  for i in range(1,q+1):
    l,r=map(int,input().split())
    for j in range(l-1,r):
      array[j]=i
    
    
        
    
  print(f"#{tc}",*array)