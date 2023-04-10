# 부품찾기
# 이진탐색으로 푼 내 답안
n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))

arr1.sort()

def binary_search(target):
  
  start,end=0,len(arr1)
  while(start<=end):
    mid=(start+end)//2
    if(arr1[mid]==target):
      return "yes"
    elif(arr1[mid]<target):
      start=mid+1
    else:
      end=mid-1
  return "no"

for req in arr2:
  print(binary_search(req),end=' ')


#계수정렬로 풀이

# N(가게의 부품 개수)을 입력받기
n=int(input())
array=[0]*1000001

#가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
  array[int(i)]=1

#손님이 확인 요청한 전체  부품 번호를 공백으로 구분하여 입력
x=list(map(int,input().split()))

#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
  #해당 부품이 존재하는지 확인
  if array[i]==1:
    print('yes',end=' ')
  else:
    print('no',end=' ')