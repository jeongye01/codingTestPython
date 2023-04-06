#떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n,m=list(map(int,input().split(' ')))
#각 떡의 개별 높이 정보를 입력받기
array=list(map(int,input().split()))

#이진 탐색을 위한 시작점과 끝점설정
start=0
end=max(array)

#이진 탐색 수행(반복적)
result=0
while(start<=end):
    total=0
    mid=(start+end)//2
    for x in array:
        #잘랐을 때의 떡의 양 계산
        if x>mid:
            total+=x-mid
    #떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total<m:
        end=mid-1
    #떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result=mid #최대한 덜 잘랐을 때가 정답이므로,여기에서 result 기록 
        start=mid+1  

# 정답 출력
print(result)

'''
내 풀이
import math
# 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값
n,m=map(int,input().split())
array=list(map(int,input().split()))

result=0 
total=0 #잘린 떡의 길이 합
array.sort(reverse=True)

for i in range(n-1):
  diff=array[i]-array[i+1] #다음으로 긴 떡과의 길이 차이
  if(total+diff*(i+1)>=m):
    result+=(m-total)/(i+1)
    break;
  else:
    total+=diff*(i+1)
    result+=diff

print(math.floor(max(array)-result)) #절단기에 설정할 수 있는 높이의 최댓값
'''