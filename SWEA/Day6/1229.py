#[S/W 문제해결 기본] 8일차 - 암호문2
#내 풀이->테스트 통과 DATE=>5.9 풀이시간 15분 
T = 10
for tc in range(1,T+1):
  n=int(input())
  codes=list(map(int,input().split()))
  m=int(input())
  oper=list(input().split())
  oper_array=[]
  idx=-1
  for i in range(len(oper)):
    if oper[i] in ["I","D"]:
      oper_array.append([oper[i]])
      idx+1
      continue
    else:
      oper_array[idx].append(int(oper[i]))
  for o in oper_array:
    if(o[0]=="I"):
      for e in reversed(o[3:]):
        codes.insert(o[1],e)
    else:
      for i in range(o[2]):
        del codes[o[1]] 
      
        
    
  print(f"#{tc}",*codes[0:10])