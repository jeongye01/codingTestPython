#공유기 설치
import math,sys
input = sys.stdin.readline
# 집의 개수(N)와 공유기의 개수(C)를 입력받기
n, c = list(map(int, input().split(' ')))

# 전체 집의 좌표 정보를 입력받기
array = []
for _ in range(n):
    array.append(int(input()))
array.sort() # 이진 탐색 수행을 위해 정렬 수행

start = 1 # 집의 좌표 중에 가장 작은 값
end = array[-1] - array[0] # 집의 좌표 중에 가장 큰 값

result = 0

if c == 2:
    print(array[n-1] - array[0])
    # 집이 2개라면 무조건 처음, 마지막 집 사이의 거리
else:
    while(start <= end):
       mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)를 의미
       value = array[0]
       count = 1
       # 현재의 mid값을 이용해 공유기를 설치
       for i in range(1, n): # 앞에서부터 차근차근 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
       if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
          start = mid + 1
          result = mid # 최적의 결과를 저장
       else:# C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
          end=mid-1
    print(result)


#두번째에도 설치로직에서 막힘. 이차원 배열에 모든 거리정보를 저장하려다가 메모리 초과 뜸. 200000이상에서 이차원 배열 만들지 말기
'''
import math,sys
input = sys.stdin.readline #이렇게 입력하기 전에 시간초과 뜸
n,c=map(int,input().split())
array=[]
for _ in range(n):
  array.append(int(input()))
array.sort()
ans=0

st=1
ed=array[-1]-array[0]
#print(distance)

while st<=ed:
  mid=(st+ed)//2
  last=c-1
  installed=0
  #그냥 앞에서 부터 차근차근 mid 이상으로 설치해보면됨
  for i in range(1,n):
    if abs(array[installed]-array[i])>=mid:
      last-=1
      installed=i
    if last<=0:
      break
      
  if last>0:
    ed=mid-1
  else:
    st=mid+1
    ans=mid
      
  

print(ans)



'''