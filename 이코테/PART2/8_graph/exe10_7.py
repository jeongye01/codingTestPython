n,m=map(int,input().split())

def find_parent(parent, x):
 if parent[x] != x:
   parent[x] = find_parent(parent, parent[x])
 return parent[x]


def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
     parent[b] = a
  else:
     parent[a] = b


parent = [0] * (n+1) # 부모 테이블 초기화
for i in range(0, n+1):
  parent[i] = i

checks=[]
for _ in range(m):
  c, a, b = map(int, input().split())
  if(c==0): #합치기 연산
    union_parent(parent, a, b)
  if(c==1): #같은 팀 여부 확인
    if(find_parent(parent,a)==find_parent(parent,b)):
      checks.append("YES")
    else:
      checks.append("NO")

for check in checks:
  print(check)
  
  