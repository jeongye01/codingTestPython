from collections import deque
#내 풀이->테스트 통과 DATE=>5.18 풀이시간 25분
def bfs(n, m, edges, s):
    # Write your code here
    graph=[[] for _ in range(1001)]
    for edge in edges:
        st,ed=edge[0],edge[1]
        graph[st].append(ed)
        graph[ed].append(st)
    visited=[-1]*(n+1)
    q=deque([(s,0)])
    visited[s]=0
    while q:
        now,dist=q.popleft()
        for node in graph[now]:
            if visited[node]==-1:
                visited[node]=dist+6
                q.append((node,dist+6))
    del visited[s]
    return visited[1:]