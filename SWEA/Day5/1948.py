# 날짜 계산기
#내 풀이->테스트 통과 DATE=>5.4 풀이시간 10분 
T = int(input())
for tc in range(1, T + 1):

  data=list(map(int,input().split()))

  dates=[0,31,28,31,30,31,30,31,31,30,31,30,31]
  ans=0
  date1=0
  date2=0
  for m in range(1,data[0]):
    date1+=dates[m]
  date1+=data[1]
  for m in range(1,data[2]):
    date2+=dates[m]
  date2+=data[3]
  ans=date2-date1+1
  
    
  
  print("#{} {}".format(tc,ans))
 