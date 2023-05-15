# https://www.acmicpc.net/problem/1072
#내 풀이->테스트 통과 DATE=>5.15 풀이시간 40분 
x,y=map(int,input().split())
st=0 #0에서 바뀌는 경우가 뭐지..?
ed=int(1e9)
ans=-1
before=int(y*100/x)


while st<=ed:
  mid=int((st+ed)//2)
  ny=y+mid
  nx=x+mid
  if before<int(ny*100/nx):
    ed=mid-1
    ans=mid
  else:
    st=mid+1
print(ans)