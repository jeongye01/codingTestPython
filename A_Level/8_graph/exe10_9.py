from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]
# 각 강의 시간을 0으로 초기화

time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보를 입력받기

for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i]) #선수과목들중에 제일 오래걸리는 것이 끝나야 해당 과목을 들을 수 있음
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v + 1):
        print(result[i])

topology_sort()




'''
#내 풀이 
from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v = int(input())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)


      

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

times=[0,]
# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1,v+1):
  array = list(map(int, input().split()))
  times.append(array[0])
  for j in array[1:-1]:
    graph[j].append(i) #j에서 i로 이동 가능 
    indegree[i] += 1


result = [] # 알고리즘 수행 결과를 담을 리스트
# 위상 정렬 함수
def topology_sort():
  
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용
    degree_zero=[]
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1): #선수 과목 없음 
        if indegree[i] == 0:
            degree_zero.append(i)
    q.append(degree_zero)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        temp=[]
        for i in now:
          for j in graph[i]:
            indegree[j] -= 1
            if(indegree[j]==0):
              temp.append(j)
        if(len(temp)>0):
           q.append(temp)
  
topology_sort()


for i in range(len(result)-1):
  for next in result[i+1]:
    max_time=0
    for now in result[i]:
      if((next in graph[now]) and max_time<times[now]):
        max_time=times[now]
    times[next]+=max_time

print(times)
  
    
    
    
  

'''