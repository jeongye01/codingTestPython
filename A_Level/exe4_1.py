#상하좌우

n=int(input())
plans=input().split()
x,y=1,1
for plan in plans:
  tempX,tempY=1,1
  if plan == "L":
    tempX,tempY = x-1,y
  elif plan == "R":
    tempX,tempY = x+1,y
  elif plan == "U":
    tempX,tempY = x,y-1
  else:
    tempX,tempY = x,y+1
  if(tempX>=1 and tempY>=1):
   
    x,y=tempX,tempY





print(x,y)