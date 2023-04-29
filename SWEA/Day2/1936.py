#1대1 가위바위보
#내 풀이->테스트 통과 DATE=>4.29 풀이시간 2분 
# 1->가위 2->바위 3->보
a,b=map(int,input().split())
if(a==1 and b==3 or a==2 and b==1 or a==3 and b==2 ):
  print("A")
else:
  print("B")