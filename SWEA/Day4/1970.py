#쉬운 거스름돈
#내 풀이->테스트 통과 DATE=>5.4 풀이시간 12분 
T = int(input())

for test_case in range(1, T + 1):
  n=int(input())
  ans=[0]*8
  money=[50000,10000,5000,1000,500,100,50,10]
  for i in range(len(money)):
    if(n==0):
      break
    ans[i]=n//money[i]
    n%=money[i]
      
  print("#{}".format(test_case)) 
  for a in ans:
    print(a,end=" ")
  print()