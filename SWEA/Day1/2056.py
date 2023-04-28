#연월일 달력
#내 풀이->테스트 통과 DATE=>4.28 풀이시간 4분 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  date=str(input())
  y=date[0:4]
  m=date[4:6]
  d=date[6:]
  max_ds=[0,31,28,31,30,31,30,31,31,30,31,30,31]
  ans=-1
  if(1<=int(m)<=12):
    if(1<=int(d)<=max_ds[int(m)]):
      ans=y+"/"+m+"/"+d
  print("#{} {}".format(test_case,ans))