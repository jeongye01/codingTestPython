#[S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
#내 풀이->테스트 통과 DATE=>4.28 풀이시간 40분 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  n,m=map(int,input().split())
  ans=0
  codes=["0001101","0011001","0010011","0111101","0100011","0110001","0101111","0111011","0110111","0001011"]
  code_row=""
  for i in range(n):
    row=str(input())
    if(row.find("1")!=-1):
      code_row=row
      
  start=code_row.find("1")
  end=len(code_row)-1-code_row[::-1].find("1")
  code="0"*(56-len(code_row[start:end+1]))+code_row[start:end+1]
  nums=[]
  for i in range(0,56,7):
    nums.append(codes.index(code[i:i+7]))
  even=0
  odd=0
  for i in range(len(nums)):
    if((i+1)%2==0):
      even+=nums[i]
    else:
      odd+=nums[i]

  ans=even+odd if (odd*3+even)%10==0 else 0
    
  print("#{} {}".format(test_case,ans))