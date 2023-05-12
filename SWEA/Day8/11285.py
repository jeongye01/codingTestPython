#다트 게임
#가운데 명중에 주의하자
import math
#내 풀이->테스트 통과 DATE=>5.10 풀이시간 30분 
T=int(input())
result=[]
for tc in range(1,T+1):
  n=int(input())
  ans=0 #점수의 합
  for _ in range(n):
    x,y=map(int,input().split())
    r=math.ceil(math.sqrt(x*x+y*y)/20)
    if r==0:
      ans+=10
    elif r<=10:
      ans+=11-r
  result.append(ans)  
for x in range(len(result)):
  print(f"#{x+1} {result[x]}")