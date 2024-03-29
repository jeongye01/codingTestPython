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
for i in range(1, n+1):
  parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0
for _ in range(m):
  a, b, c= map(int, input().split())
  edges.append((c, a, b))

edges.sort()

last = 0
result=0
for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result+=cost
    last=cost
     

print(result-last)