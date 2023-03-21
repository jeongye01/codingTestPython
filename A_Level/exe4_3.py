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



