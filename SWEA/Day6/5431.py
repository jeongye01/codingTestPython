# 민석이의 과제 체크하기
#내 풀이->테스트 통과 DATE=>5.9 풀이시간 10분 
T = int(input())
for tc in range(1,T+1):
  n,k=map(int,input().split())
  array=[i for i in range(1,n+1)]
  submitted=list(map(int,input().split()))
  result=[]
  for a in array:
    if(a not in submitted):
      result.append(a)
    
  print(f"#{tc}",*result)