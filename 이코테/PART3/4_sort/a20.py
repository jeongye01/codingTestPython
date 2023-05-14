#실패율
def solution(N, stages): 
    answer = []
    length = len(stages)
    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count
    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer


'''
내 풀이->테스트 통과 DATE-> 4.22 풀이시간->30분 

def solution(N, stages):

    #실패율 -> 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    players=len(stages)
    stages.sort()
    array=[0]*N
    for i in range(len(stages)):
        if stages[i]<=N:
            array[stages[i]-1]+=1
        
    result=[]
    for i in range(N):
        result.append([array[i]/players if players>0 else 0,i+1])
        players-=array[i]
    result.sort(key=lambda x:(-x[0],x[1]))   
    answer=[]
    for res in result:
        answer.append(res[1])

    return answer

'''
#내 풀이->테스트 통과 DATE-> 5.15 풀이시간->25분 
'''
def solution(N, stages): 
    answer = []
    stages.sort()
    member=len(stages)
    result=[[0,i] for i in range(N+1)] #실패 한 사람 수,스테이지 번호
    for s in stages:
        if s<=N:
            result[s][0]+=1
    for i in range(1,N+1):
        cnt=result[i][0]
        result[i][0]=result[i][0]/member
        member-=cnt
        if member==0:
            break
    result=result[1:]
    result.sort(key=lambda x:-x[0])
    for r in result:
        answer.append(r[1])

            
    return answer


'''