#신뢰
#내 풀이->테스트 통과 DATE=>5.19 풀이시간 120분 
from collections import deque
T=int(input())
for tc in range(1,T+1):
    arr=list(input().split())
    n=int(arr[0]) #버튼을 누르는 경우의 수
    b_move=deque()
    o_move=deque()
    order=deque()
    for i in range(1,len(arr),2):
        #print(arr[i])
        if arr[i]=="B":
            b_move.append(int(arr[i+1]))
        if arr[i]=="O":
            o_move.append(int(arr[i+1]))
        order.append(arr[i])

    time=0
    b_pos=1
    o_pos=1

    while order:
        now=order.popleft()
        if now=="B":
            b = b_move.popleft() # 이동시키기
            time+=abs(b_pos-b)+1

            if o_move:
                o = o_move.popleft()
                if o>o_pos:
                    o_pos+=(abs(b_pos - b) + 1)
                    o_pos=o if o<o_pos else o_pos
                else:
                    o_pos -= (abs(b_pos - b) + 1)
                    o_pos = o if o > o_pos else o_pos

                o_move.appendleft(o)

            b_pos = b
        else:
            o = o_move.popleft()  # 이동시키기
            time += abs(o_pos - o )+1

            if b_move:
                b = b_move.popleft()
                if b > b_pos:
                    b_pos += abs(o_pos - o) + 1
                    b_pos = b if b < b_pos else b_pos
                else:
                    b_pos -= (abs(o_pos - o) + 1)
                    b_pos = b if b > b_pos else b_pos
                b_move.appendleft(b)
            o_pos = o

    print(f"#{tc} {time}")