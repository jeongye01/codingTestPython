#알파벳을 숫자로 변환
#내 풀이->테스트 통과 DATE=>5.1 풀이시간 5분 
T = 1

for test_case in range(1, T + 1):
  
  s=input()
  ans=[]
  for x in s:
    ans.append(ord(x)-ord('A')+1)
  for a in ans:
    print(a,end=" ")