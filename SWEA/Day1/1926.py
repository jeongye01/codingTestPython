# 간단한 369게임
#내 풀이->테스트 통과 DATE=>4.28 풀이시간 8분 


T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    ans=""
    for s in range(1,n+1):
      cnt=0
      ns=str(s)
      for i in range(len(str(ns))):
        if(ns[i]=="3" or ns[i]=="6" or ns[i]=="9"):
          cnt+=1
      if(cnt>0):
        ans+=" "+"-"*cnt
      else:
        ans+=" "+str(s)
    print(ans.strip())
    #print("#{} {}".format(test_case,ans))