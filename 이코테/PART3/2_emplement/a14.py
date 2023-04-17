# weak 리스트와dist 리스트의길이가매우작은것을알수있다. 
#문제 풀이를 간단히 하기 위하여 길이를 2배로 늘려서 ‘원형’을 일 자 형태로 만드는 작업을 해주면 유리하다.
from itertools import permutations
def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer





'''
# 내풀이 -> 테스트 통과   DATE->4.16 
import copy

def count(weak,dist,n):
    if(len(weak)==0):
        return 0
    if(len(dist)==0):
        return 1e9
    res=1e9
    p=-1
    for w in weak:
      p+=1
      if(w+dist[0]<weak[(p+1)%len(weak)]):
        continue
      tmpWeak=copy.deepcopy(weak)
      start=w
      for i in range(0,dist[0]+1):
        if (start+i)%n in weak:
          tmpWeak.remove((start+i)%n)
      res=min(res,count(tmpWeak,dist[1:],n)+1)

    return res
        

def solution(n, weak, dist):
    dist.sort(reverse=True)
    answer = count(weak,dist,n) #취약 지점을 점검하기 위해 보내야하는 친구 수 
    if(answer>len(dist)):
        answer=-1
    
        
    return answer
'''