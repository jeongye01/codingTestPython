# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))
data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수 second = data[n - 2] # 두 번째로 큰 수
# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k 
count+= m%(k+1)
result = 0
result += (count) * first # 가장 큰 수 더하기 result+= (m-count)*second#두번째로큰수더하기
print(result) # 최종 답안 출력
 


'''
# 내풀이 
# 가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산
n,m,k=map(int,input().split())
array=list(map(int,input().split()))


array.sort(reverse=True)
result=0
cnt=k
first = array[0] # 가장 큰 수 
second = array[1] # 두 번째로 큰 수
for i in range(m):
  if(cnt==0):
    result+=second
    cnt=k
  else:
    result+=first 
    cnt-=1
    

print(result)

'''