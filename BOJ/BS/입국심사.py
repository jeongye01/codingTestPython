import sys
#https://www.acmicpc.net/problem/3079
##내 풀이->테스트 통과 DATE=>5.15 풀이시간 60분 
input=sys.stdin.readline
n,m=map(int,input().split())


arr=[]
for _ in range(n):
  arr.append(int(input()))
arr.sort()
st=0
ed=1000000000*m

ans=0
while st<=ed:
  mid=(st+ed)//2
  processed=0
  success=False
  for a in arr:
    #print(mid%a,mid,a,"??")
    processed+=(mid//a)
    if processed>=m:
      success=True
      break
  #print(processed,mid)
  if success:
    ans=mid
    ed=mid-1
  else:
    st=mid+1


print(ans)