#파스칼의 삼각형
#내 풀이->테스트 통과 DATE=>4.29 풀이시간 15분 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  n=int(input())
  ans=[]
  for i in range(1,n+1):
    tmp=[]
    for j in range(1,i+1):
      if(j==1 or j==i):
        tmp.append(1)
      else:
        tmp.append(ans[i-2][j-2]+ans[i-2][j-1])
    ans.append(tmp)
  print("#{}".format(test_case))
  for i in ans:
    print(*i)