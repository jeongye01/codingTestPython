
'''
#내풀이 -> 테스트 통과  DATE->4.20 풀이시간->40분
from itertools import combinations


answer="NO"
n=int(input())
board=[]
emptys=[]
teachers=[]
students=[]
for y in range(n):
  data=list(input().split())
  board.append(data)
  for x in range(n):
    if(data[x]=="X"):
      emptys.append((x,y))
    elif(data[x]=="T"):
      teachers.append((x,y))
    elif(data[x]=="S"):
      students.append((x,y))


dx=[0,-1,0,1]
dy=[-1,0,1,0]
def check():
  global teachers
  for teacher in teachers:
    x,y=teacher
    for d in range(4):
      if(found(x,y,d)):
        return "NO"
  return "YES"
      

def found(x,y,d):
  global board
  if(x<0 or x>=n or y<0 or y>=n):
    return False
  if(board[y][x]=="O"):
    return False
  if(board[y][x]=="S"):
    return True  
  x,y=x+dx[d],y+dy[d]
  return found(x,y,d)
    
    


for obs in list(combinations(emptys,3)):
  for i in range(3):
    (x,y)=obs[i]
    board[y][x]="O"
  if(check()=="YES"):
    answer="YES"
    break
  for i in range(3):
    (x,y)=obs[i]
    board[y][x]="X"
    
  
print(answer)


'''