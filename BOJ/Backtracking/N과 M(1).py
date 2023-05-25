#https://www.acmicpc.net/problem/15649

#내 풀이->테스트 통과 DATE=>5.22 풀이시간 10분 
n,m=map(int,input().split())

def bt(arr):
  if len(arr)==m:
    print(*arr)
    return
  for i in range(1,n+1):
    if i not in arr:
      bt(arr+[i])
    


bt([])