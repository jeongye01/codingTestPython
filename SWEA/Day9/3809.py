#화섭이의 정수 나열
#내 풀이->테스트 통과 DATE=>5.18 풀이시간 60분 
#줄바꿈 입력이 존재하는지 유의하자
T=int(input())

for tc in range(1,T+1):
  n=int(input())
  arr=[]
  while len(arr)<n:
    arr.extend(list(map(str,input().split())))
  string="".join(arr)
  ans=-1
  while True:
    ans+=1
    if string.find(str(ans))==-1:
      break
  
      
  print(f"#{tc} {ans}")
    