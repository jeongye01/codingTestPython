def possble(answer):
    for x,y,stuff in answer:
        if stuff==0: #설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위'혹은 '다른 기둥 위'라면 정상
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False #아니라면 (False)반환
        elif stuff==1:
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝 부분이 다른 보와 동시에 '연결'이라면 정상
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return False

def solution(n,build_frame):
    answer=[]
    for frame in build_frame:
        x,y,stuff,operate=frame
        if operate==0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        if operate==1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)



'''
# 내풀이 -> 오답  DATE->4.16 
def solution(n, build_frame):
    answer = []
    
    #기둥,보,로봇의 동작을 시뮬레이션 할 수 있는 프로그램
    #  기둥과 보는 길이가 1인 선분으로 표현
    #삭제 가능
    # 조건을 만족하지 않는다면 해당 작업은 무시됨.
    # build_frame 기둥과 보를 설치하거나 삭제하는 작업이 순서 [x, y, a, b]
    # x,y-> 기둥,보를 설치 또는 삭제할 교차점의 좌표 x-> col
    # a-> 1-> 기둥 0 -> 보
    # b-> 0-> 삭제 1-> 설치
    # todo: 설치 or 제거 V
    # todo: 조건 확인
    # todo: 결과 출력 
    memory=[[[0,0]]*(n+1) for _ in range(n+1)]
    result=[]
    for work in build_frame:
        x=work[0]
        y=work[1]
        a=work[2]
        b=work[3]
        if(b==1): # 기둥 or 보 설치 
            if(a==1): #보인 경우
                # 양 옆에 보가 있는가?
                #오른쪽 -> memory[y][x+1][0]
                #왼쪽 -> memory[y][x-1][0]
                #양 옆에 기둥이 있는가?
                #오른쪽 -> memory[y][x+1][1]
                #왼쪽 -> memory[y][x-1][1]
                if(x==0 and memory[y-1][x][0]==0 and memory[y-1][x+1][0]==0):
                    continue
                if(x==n and memory[y-1][x][0]==0 and memory[y-1][x-1][0]==0):
                    continue
                if(memory[y-1][x][0]==0 and memory[y-1][x+1][0]==0 and (memory[y][x-1][1]==0 or memory[y][x+1][1]==0)): 
                    continue
            else:
                if(y-1>=0 and x==0 and memory[y-1][x][0]==0 and memory[y][x][1]==0 ):
                    continue
                if(y-1>=0 and x==n and memory[y-1][x][0]==0 and memory[y][x-1][1]==0 ):
                    continue
                if(y-1>=0 and memory[y-1][x][0]==0 and memory[y][x][1]==0 and   memory[y][x-1][1]==0):
                    continue
            memory[y][x][a]=1
            result.append((x,y,a))
        
    
        else: #기둥 or 보 제거 
            if(a==1): #보인 경우
                  # 양 옆에 보가 있으면. 기둥을 가지고 있는가
                  
                    if(x<=n-1 and memory[y][x+1][1]==1 and memory[y-1][x+1][0]==0 and (x+2<=n and memory[y-1][x+2][0]==0)):
                        continue
                    if(x-1>=0 and memory[y][x-1][1]==1 and memory[y-1][x][0]==0 and memory[y-1][x-1][0]==0):
                        continue


            else: #기둥인 경우
                # 보가 있고, 해당 보 양옆에 보 or 기둥이 있는가?
                if( x==n and memory[y+1][x-1][1]==1 and memory[y][x-1][0]==1):
                    continue
                if( x==0 and memory[y+1][x][1]==1 and memory[y][x+1][0]==1):
                    continue
                if( memory[y+1][x][1]==1  and memory[y][x+1][0]==0 and (memory[y+1][x+1][1]==0 or memory[y+1][x-1][1]==0)):
                    continue
                if(memory[y+1][x-1][1]==1  and memory[y][x-1][0]==0 and (memory[y+1][x][1]==0 or x-2>=0 and memory[y+1][x-2][1]==0)):
                    continue
            if ((x,y,a) in result):
                memory[y][x][a]=0
                result.remove((x,y,a))

    result.sort(key=lambda x: (x[0], x[1],x[2]))
    answer=result
                    

    return answer

'''