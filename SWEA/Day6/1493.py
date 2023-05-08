#수의 새로운 연산
#내 풀이->테스트 통과 DATE=>5.8 풀이시간 30분 
T = int(input())

def sol():
  dots=[[]]
  global ans
  pos1=(-1,-1)
  pos2=(-1,-1)
  pos3=(-1,-1)
  cnt=0
  #print(pos3)
  i=1
  while True:

      for j in range(1,i+1):
        cnt+=1
        dots.append([j,i-j+1])
        #print(dots)
        if(cnt==a):
          pos1=(j,i-j+1)
        if(cnt==b):
          pos2=(j,i-j+1)
        if(pos1!=(-1,-1) and pos2!=(-1,-1)):
          pos3=(pos1[0]+pos2[0],pos1[1]+pos2[1])
        if(pos3==(j,i-j+1)):
          ans=cnt
          break
      if(ans!=0):
        break
      i+=1
for tc in range(1,T+1):
  ans=0
  a,b=map(int,input().split())
  sol()
  
  print(f"#{tc}",ans)