import heapq

n = int(input())
# 힙(Heap)에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0
# 힙(Heap)에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)




'''
내 풀이->테스트 통과 DATE-> 4.22 풀이시간->30분 
import heapq
n=int(input())
hq=[]
for  _ in range(n):
    heapq.heappush(hq,int(input()))

if(n==1):
    print(0)
else:
    result=0
    while len(hq)>2:
        card1=heapq.heappop(hq)
        card2=heapq.heappop(hq)
        card3=card1+card2
        result+=card3
        heapq.heappush(hq,card3)
        #print(q)
    res1=heapq.heappop(hq)
    res2=heapq.heappop(hq)
    result+=(res1+res2)
    print(result)

'''