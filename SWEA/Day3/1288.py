#새로운 불면증 치료법
#내 풀이->테스트 통과 DATE=>5.2 풀이시간 10분 
T = int(input())
for test_case in range(1, T + 1):
  n=int(input())
  i=1
  nums=[0]*10
  while True:
    for x in str(n*i):
      nums[int(x)]=1
    if(nums.count(0)==0):
      ans=n*i
      break
    i+=1
    
  print("#{} {}".format(test_case,ans)) 