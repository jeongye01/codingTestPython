
#원재의 메모리 복구하기
#내 풀이->테스트 통과 DATE=>5.4 풀이시간 9분 
T = int(input())

for test_case in range(1, T + 1):
  s=input()
  flag="1"
  recover="0"*len(s)
  ans=0
  for i in range(len(s)):
    if(s[i]==flag):
      recover=recover[:i]+flag*(len(s)-i)
      ans+=1
      flag="1" if flag=="0" else "0"
  #print(recover)
  
  print("#{} {}".format(test_case,ans))
