#알파벳 공부
#내 풀이->테스트 통과 DATE=>5.10 풀이시간 5분 
T = int(input())
for tc in range(1, T + 1):
  s=input()
  ans=0
  alpa="abcdefghijklmnopqrstuvwxyz"
  for i in range(len(s)):
    if alpa[i]==s[i]:
      ans+=1
    else:
      break
  
        
    
  print(f"#{tc} {ans}")