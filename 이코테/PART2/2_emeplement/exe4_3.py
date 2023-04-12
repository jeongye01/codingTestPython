#내풀이 4.12
result=0 # 나이트가 이동할수 있는 경우의 수 

pos=input()

x,y=ord('a')-ord(pos[0])+1,int(pos[1])

moves=[(2,-1),(2,1),(-2,-1),(-2,1),(-1,2),(1,2),(-1,-2),(1,2)]

for m in moves:
  tempX,tempY=x-m[0],y-m[1]
  if(tempX<1 or tempX>8 or tempY<1 or tempY>8):
    continue
  result+=1

print(result)

'''
내 풀이  3.20
#왕실의 나이트
input_data = input()


x,y=int(ord(input_data[0])) - int(ord('a'))+1,int(input_data[1])
result=0
steps = [(-2, -1 ), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
for step in steps:
  tempX,tempY=x+step[0],y+step[1]
  if(tempX>=1 and tempY>=1 and tempX<=8 and tempY<=8):
    result+=1
print(result)

'''



