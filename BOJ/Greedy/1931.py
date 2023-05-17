#https://www.acmicpc.net/problem/1700
#https://hongcoding.tistory.com/22
#1.앞으로 사용할 예정에 없음 2.제일 나중에 쓸거임 순서로 뽑는다
#멀티탭 스케줄링
##내 풀이->테스트 통과 DATE=>5.17 풀이시간 60분 
n=int(input())
meetings=[]

for _ in range(n):
  st,ed=map(int,input().split())
  meetings.append([st,ed])
meetings.sort(key=lambda x:(x[0],x[1]))
#for m in meetings:
 # print(m)

cnt=1
last=0
for i in range(1,n):
  if meetings[last][1]<=meetings[i][0] :
    cnt+=1
    last=i
  elif meetings[last][1]>=meetings[i][1] :
    last=i
   
print(cnt)