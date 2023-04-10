# 정수 N을 입력받기
n=int(input())
#모든 식량 정보 입력받기
array=list(map(int,input().split()))

#앞서 계산된 결과를저장하기 위한 DP테이블 초기화
d=[0]*100

#다이나믹 프로그래밍 진행(bottom up)
d[0]=array[0]
d[1]=max(array[0],array[1])
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+array[i])

print(d[n-1])

'''
# 내풀이
#최소 한칸 이상 떨어진 식량창고를 약탈해야함

n=int(input()) #식량 창고 개수
array=list(map(int, input().split()))

d=[0]*n
result=0
for i in range(0,n):
  maximum=0
  for j in range(i+2,n):
    if(d[j]!=0):break;
    if(maximum<array[j]):
      maximum=array[j]
  d[i]+=array[i]+maximum
  
print(max(d))


'''