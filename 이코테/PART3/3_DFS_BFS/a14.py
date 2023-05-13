# 연산자 끼워 넣기
n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9 
max_value = -1e9

# 깊이 우선 탐색(DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i])) # 나눌 때는 나머지를 제거
            div += 1
# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value) 
print(min_value)


'''
#내풀이 -> 테스트 통과  DATE->4.20 풀이시간->60분
from itertools import product



n=int(input())
nums=list(map(int,input().split()))
add, sub, mul, div = map(int, input().split())




def operate(perm):
  result=nums[0]
  for i in range(1,len(nums)):
    if(perm[i-1]=="+"):
        result+=nums[i]
    elif(perm[i-1]=="-"):
        result-=nums[i]
    elif(perm[i-1]=="*"):
        result*=nums[i]
    elif(perm[i-1]=="/"):
        if(result<0):
            result=-1*((-1*result)//nums[i])
        else:
            result//=nums[i]
  return result
minimum=1e9
maximum=-1e9
    
for perm in list(product(['+','-','*','/'], repeat=(n - 1))):
    if(list(perm).count('+')>add):
        continue
    if(list(perm).count('-')>sub):
        continue
    if(list(perm).count('/')>div):
        continue
    if(list(perm).count('*')>mul):
        continue
     
    minimum=min(minimum,operate(list(perm)))
    maximum=max(maximum,operate(list(perm)))


print(maximum)
print(minimum)


#내풀이1->시간초과
from itertools import permutations



n=int(input())
nums=list(map(int,input().split()))
add, sub, mul, div = map(int, input().split())


opers_array=[]

for i in range(add):
  opers_array.append("+")
for i in range(sub):
  opers_array.append("-")
for i in range(mul):
  opers_array.append("*")
for i in range(div):
  opers_array.append("/")



def operate(perm):
  result=nums[0]
  for i in range(1,len(nums)):
    if(perm[i-1]=="+"):
        result+=nums[i]
    elif(perm[i-1]=="-"):
        result-=nums[i]
    elif(perm[i-1]=="*"):
        result*=nums[i]
    elif(perm[i-1]=="/"):
        if(result<0):
            result=-1*((-1*result)//nums[i])
        else:
            result//=nums[i]
  return result
minimum=1e9
maximum=0
    
for perm in list(permutations(opers_array, len(nums)-1)):
    print(list(perm))
    minimum=min(minimum,operate(list(perm)))
    maximum=max(maximum,operate(list(perm)))


print(maximum)
print(minimum)

'''
#내풀이 -> 테스트 통과  DATE->5.12 풀이시간->40분
'''
def bt(idx,v,path):
  global mx,mn,opes
  if idx>=n:
    #print(opes,path,v)
    mx=max(mx,v)
    mn=min(mn,v)
    return
  #print(v)
  if opes[0]>0:
    opes[0]-=1
    bt(idx+1,v+arr[idx],path+[0])
    opes[0]+=1
  if opes[1]>0:
    opes[1]-=1
    bt(idx+1,v-arr[idx],path+[1])
    opes[1]+=1
  if opes[2]>0:
    opes[2]-=1
    bt(idx+1,v*arr[idx],path+[2])
    opes[2]+=1
  if opes[3]>0:
    opes[3]-=1
    tmp=v
    if v<0:
      tmp=(-1)*(abs(v)//arr[idx])
    else:
      tmp=v//arr[idx]
    bt(idx+1,tmp,path+[3])
    opes[3]+=1


n=int(input())
arr=list(map(int,input().split()))
opes=list(map(int,input().split())) #덧셈,뺄셈,곱셈,나눗셈
mx,mn=-1e9,1e9
bt(1,arr[0],[])
print(mx)
print(mn)



'''