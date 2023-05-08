# 영준이의 카드 카운팅
#내 풀이->테스트 통과 DATE=>5.9 풀이시간 13분 
T = int(input())
for tc in range(1,T+1):
  dict={"S":0,"D":1,"H":2,"C":3}
  result=[13,13,13,13]
  collect=[[],[],[],[]]
  s=input()
  isError=False
  for i in range(0,len(s),3):
    if(int(s[i+1:i+3]) in collect[dict[s[i]]]):
      isError=True
      break
    collect[dict[s[i]]].append(int(s[i+1:i+3]))
    result[dict[s[i]]]-=1
    
  if(not isError):
    print(f"#{tc}",*result)
  else:
    print(f"#{tc}","ERROR")