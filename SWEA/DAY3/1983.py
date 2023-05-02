#조교의 성적 매기기
#내 풀이->테스트 통과 DATE=>5.2 풀이시간 40분 
import math
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  grades=["","A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
  n,k=map(int,input().split())
  array=[list(map(int,input().split())) for _ in range(n)]

  points=[]
  for i in range(n):
    points.append(array[i][0]*0.35+array[i][1]*0.45+array[i][2]*0.2)
  p=points[k-1]
  #print(points)
  points.sort(reverse=True)
  order=points.index(p)+1
  #print(order,points)
  ans=grades[math.ceil((order/n)*10)]
  
    
  

  
    
  print("#{} {}".format(test_case,ans))