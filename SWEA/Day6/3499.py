#퍼펙트 셔플
#내 풀이->테스트 통과 DATE=>5.6 풀이시간 20분 
T = int(input())
for tc in range(1,T+1):
  n= int(input())
  data=list(input().split())
  result=[]
  if n%2==1:
    result=[data[0]]
    data=data[1:]
  set1=data[0:n//2]
  set2=data[n//2:]
  if n%2==1:
    first,second=set2,set1
  else:
    first,second=set1,set2
  for i in range(n//2):
    result.extend([first[i],second[i]])
    
  print(f"#{tc}",*result)