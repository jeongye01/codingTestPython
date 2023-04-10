# 플로이셜로 풀이
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정


# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행

for k in range(1, n + 1):
 for a in range(1, n + 1):
  for b in range(1, n + 1):
    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
   print("-1")
# 도달할 수 있다면, 최단 거리를 출력
else: 
   print(distance)


'''
# 내풀이(다익스트라 사용)

import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

# n->노드 수 m->간선 수 
n,m=map(int,input().split())
graph=[[]for i in range(n+1)]


for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))
  
# x->가야하는 회사 k->소개팅 장소
x,k=map(int,input().split())

def dijkstra(start,end):
    distance=[INF]*(n+1)
    q=[]
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q: #큐가 비어있지 않다면
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist,now=heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now]<dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost=dist+i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance[end]


result=dijkstra(1,k)+dijkstra(k,x)
if result>=INF:
  print(-1)
else:
  print(result)

'''