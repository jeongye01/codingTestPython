#중간 평균값 구하기
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  
  array=list(map(int,input().split())) 

  ans=round((sum(array)-max(array)-min(array))/(len(array)-2))

    
  

  
    
  print("#{} {}".format(test_case,ans))