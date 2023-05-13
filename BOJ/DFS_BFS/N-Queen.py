n=int(input())
record=[-1]*n
cnt=0
#9663
#https://www.acmicpc.net/problem/9663
#내 풀이->테스트 통과 DATE=>5.13 풀이시간 50분 
visited=[False]*n
def bt(idx):
  global ans,record,cnt,visited
  
  
  if idx==n:
    #print(record)
    ans+=1
    return
  #print(record)
  for i in range(n):
    if not visited[i]:
      dia=True
      for j in range(idx):
        if abs(record[j]-i)==abs(j-idx):
          dia=False
          break
      if dia:
        record[idx]=i
        visited[i]=True
        bt(idx+1)
        visited[i]=False
      
      
        
      
  
      
ans=0
bt(0)
print(ans)