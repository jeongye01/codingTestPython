#어디에 단어가 들어갈 수 있을까
#내 풀이->테스트 통과 DATE=>5.1 풀이시간 50분 
# 011101110 일때. s.count("01110")은 1을 리턴함
T = int(input())

for test_case in range(1, T + 1):
  n,m=map(int,input().split())
  board=[]
  for _ in range(n):
    board.append(list(input().split())) 
  ans=0
  for i in range(n):
    s="".join(board[i])
    if(s[0:m+1]=="1"*m+"0"):
      ans+=1
    if(s[::-1][0:m+1]=="1"*m+"0"):
      ans+=1
    for i in range(0,n-(m+1)):
      if(s[i:i+m+2]=="0"+"1"*m+"0"):
        ans+=1

  for i in range(n):
    s=""
    for j in range(n):
      s+=board[j][i]
    if(s[0:m+1]=="1"*m+"0"):
      ans+=1
    if(s[::-1][0:m+1]=="1"*m+"0"):
      ans+=1
    for i in range(0,n-(m+1)):
      if(s[i:i+m+2]=="0"+"1"*m+"0"):
        ans+=1


  
   
  
  print("#{} {}".format(test_case,ans))