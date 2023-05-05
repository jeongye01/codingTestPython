#최장 경로
##내 풀이->테스트 통과 DATE=>5.5 풀이시간 50분 
T = int(input())

def dfs(v,visited):
  global ans
  if(len(visited)>ans):
    ans=len(visited)
  for i in graph[v]:
    if i not in visited:
      dfs(i,visited+[i])

for tc in range(1, T + 1):
  tmp=0
  n,m=map(int,input().split())
  graph=[[]*(n+1) for _ in range(n+1)]
  ans=0
  for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
  
  for i in range(1,n+1):
    dfs(i,[i]) 
  print("#{} {}".format(tc,ans))