# 시각
n=int(input())

x=0; #3이 없는 시의 수
y=0; #3이 없는 초 or 분의 수
for i in range(n+1):
  if(str(i).find("3")==-1): 
    x+=1

for i in range(60):
  if(str(i).find("3")==-1): 
    y+=1

print((n+1)*60*60-x*y*y)
