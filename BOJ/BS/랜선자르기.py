# https://www.acmicpc.net/problem/1654
#내 풀이->테스트 통과 DATE=>5.15 풀이시간 15분 
k,n=map(int,input().split())

arr=[]
for _ in range(k):
  arr.append(int(input()))
ans=-1
st=1
ed=max(arr)
while st<=ed:
  lines=[]
  mid=(st+ed)//2
  for a in arr:
    cut=a
    while cut>=mid:
      lines.extend([mid])
      cut-=mid
  #print(lines,mid)
  if lines.count(mid)>=n:
    st=mid+1
    ans=mid
  else:
    ed=mid-1
print(ans)