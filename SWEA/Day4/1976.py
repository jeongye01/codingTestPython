#시각 덧셈
##내 풀이->테스트 통과 DATE=>5.5 풀이시간 5분 
T = int(input())
for tc in range(1, T + 1):

  data=list(map(int,input().split()))
  h=data[0]+data[2]
  m=data[1]+data[3]
  if(m//60>0):
    h+=m//60
    m=m%60
  if(h%12!=0):
    h%=12
  if(h==24):
    h=12
  
  print("#{} {} {}".format(tc,h,m))