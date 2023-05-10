#소득 불균형
#내 풀이->테스트 통과 DATE=>5.10 풀이시간 10분 
T = int(input())
for tc in range(1, T + 1):
  n=int(input())
  array=list(map(int,input().split()))
  array.sort()
  mean=sum(array)/n
  ans=0
  start,end=0,n-1
  while start<=end:
    mid=(start+end)//2
    if(array[mid]<=mean):
      start=mid+1
      ans=mid
    else:
      end=mid-1
  
        
    
  print(f"#{tc} {ans+1}")