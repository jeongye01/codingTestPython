#간단한 소인수분해
#내 풀이->테스트 통과 DATE=>5.2 풀이시간 10분 
from itertools import product
nums=[i for i in range(0,10)]
prod=list(product(nums, repeat=5))
T = int(input())

for test_case in range(1, T + 1):
  n=int(input())
  ans=[]
  for p in prod:
    if(n==pow(2,p[0])*pow(3,p[1])*pow(5,p[2])*pow(7,p[3])*pow(11,p[4])):
      ans=p
    
  
    
  print("#{}".format(test_case),end=" ")
  for a in ans:
     print(a,end=" ")
  print()
    
#print(pow(2,3)*pow(3,2)*pow(5,2)*pow(7,3)*pow(11,1))