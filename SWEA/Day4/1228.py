#[S/W 문제해결 기본] 8일차 - 암호문1
#내 풀이->테스트 통과 DATE=>5.4 풀이시간 30분 
T = 10
for test_case in range(1, T + 1):
  n=int(input())
  array=list(map(int,input().split()))
  m=int(input())#명령어 개수
  c=list(input().split())
  ans=0
  i=0
  x,y=0,0
  while m>0:
    #print(i)
    if(c[i]=="I"):
      x,y=int(c[i+1]),int(c[i+2])
      #print(c[i+3:i+2+y+1])
      array=array[0:x]+c[i+3:i+2+y+1]+array[x:]
      i+=(3+y)
      m-=1
      
    
  print("#{}".format(test_case),end=" ")
  for a in array[0:10]:
    print(a,end=" ")
  #print()