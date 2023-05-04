#가랏! RC카!
#내 풀이->테스트 통과 DATE=>5.4 풀이시간 16분 
T = int(input())
for tc in range(1, T + 1):
  n=int(input())
  array=[]
  ans=0
  v=0
  for i in range(n):
    array.append(list(map(int,input().split())))
  for i in range(n):
    if(array[i][0]==0):
      ans+=v
    elif(array[i][0]==1): #가속
      v+=array[i][1]
      ans+=v
    else:#감속
      v-=array[i][1]
      if(v<0):
        v=0
      ans+=v
      
    

  print("#{} {}".format(tc,ans))