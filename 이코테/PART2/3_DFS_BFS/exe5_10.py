#다시 보기 필요
#음료수 얼려먹기


n,m=map(int,input().split())
graph=[list(map(int, input().split())) for _ in range(m)]



def dfs(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  if graph[x][y]==0:
    graph[x][y]=1
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

result=0
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      result+=1
print(result)
  
'''
내 풀이
n,m=map(int,input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

dx=[0,-1,0,1]
dy=[-1,0,1,0]
answer=0
def dfs(x,y):
  if(graph[y][x]==1):
    return
  graph[y][x]=1
  for d in range(4):
    newX,newY=x+dx[d],y+dy[d]
    if(newX>=0 and newX<m and newY>=0 and newY<n):
      dfs(newX,newY)
  
for i in range(n):
  for j in range(m):
    if(graph[i][j]==1):
      continue
    else:
      answer+=1
      dfs(j,i)

print(answer)

'''

