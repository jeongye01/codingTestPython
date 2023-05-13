
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

##내풀이 -> 테스트 통과  DATE->5.13 풀이시간->60분 ->입력방식에 주의하자!!!!
'''
from itertools import combinations

n=int(input())
board=[]
idxs=[]
dx=[0,-1,0,1]
dy=[-1,0,1,0]
def check(x,y,d):

  global visited,board

  if x<0 or x>=n or y<0 or y>=n:
    #print("?",x,y,len(board))
    return True
  elif board[y][x]=="S":
    #print("S",x,y)
    return False
  elif board[y][x]=="O":
    #print("O",x,y,board[y][x])
    return True

  return check(x+dx[d],y+dy[d],d)

def solution():
  for i in range(n):
    for j in range(n):
      #print(i,j,"tlqkf?",n,board[i][j])
      if board[i][j]=="T":
          #print(i,j,"선생",n)
          for d in range(4):
            if not check(j,i,d):
              #print(j,i,"미통과")
              return False
       
  return True
    
  
for i in range(n):
  data=list(input().split())
  for j in range(n):
    if data[j]=="X":
      idxs.append((j,i))
  board.append(data)
  
comb=list(combinations(idxs,3))
ans="NO"
for c in comb:
  for o in c:
    tx,ty=o
    board[ty][tx]="O"
  #for b in board:
   #   print(*b)
  if solution()==True:
    ans="YES"
    
    break
  for o in c:
    tx,ty=o
    board[ty][tx]="X"
    

print(ans)


'''