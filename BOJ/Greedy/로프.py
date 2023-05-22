#https://www.acmicpc.net/problem/2217
##내 풀이->테스트 통과 DATE=>5.22 풀이시간 10분 
ans=0 #들어올릴 수 있는 물체의 최대 중량

n=int(input())
arr=[]
for _ in range(n):
  arr.append(int(input()))

ans=0
arr.sort()
for i in range(n):
  ans=max(ans,arr[i]*(n-i))
  

print(ans)