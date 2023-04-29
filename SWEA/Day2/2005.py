#파스칼의 삼각형
#내 풀이->테스트 통과 DATE=>4.29 풀이시간 15분 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  
  n=int(input())
  ans=[]
  ans.append([1])

  for i in range(1,n):
    tmp=[0]*(i+1)
    tmp[0],tmp[-1]=1,1
    for j in range(1,i):
      tmp[j]=ans[i-1][j-1]+ans[i-1][j]
    ans.append(tmp)
  print("#{}".format(test_case))
  for r in ans:
    for c in r:
      print(c,end=" ")
    print()