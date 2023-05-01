#숫자 배열 회전
#내 풀이->테스트 통과 DATE=>5.1 풀이시간 10분 
T = int(input())

for test_case in range(1, T + 1):
  n=int(input())
  array=[list(input().split()) for _ in range(n)]
  print("#{}".format(test_case))
  ans=[[""]*n for _ in range(n)]
  for i in range(3):
    array = list(map(list, zip(*array[::-1])))
    for j in range(n):
        ans[j][i]="".join(array[j])

 
  for i in ans:
    print(*i)