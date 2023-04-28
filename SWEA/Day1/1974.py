# 스도쿠 검증
#내 풀이->테스트 통과 DATE=>4.28 풀이시간 20분 
def check1(board):
  for i in range(9):
    nums1=[]
    nums2=[]
    for j in range(9):
      if((board[i][j]  in nums1) or (board[j][i]  in nums2)):
        return False
      else:
        nums1.append(board[i][j])
        nums2.append(board[j][i])
  return True

def check2(board):
  for i in range(0,9,3):
      for j in range(0,9,3):
        nums=[]
        for a in range(0,3):
          for b in range(0,3):
           if( board[i+a][j+b] in nums):
             return False
           else:
             nums.append(board[i+a][j+b])
  return True


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  board=[]
  ans=1
  for _ in range(9):
    board.append(list(map(int,input().split())))
  
  
  if not check1(board):
    ans=0
  elif not check2(board):
    ans=0
    
    
  print("#{} {}".format(test_case,ans))