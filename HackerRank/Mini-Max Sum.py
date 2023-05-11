#내 풀이->테스트 통과 DATE=>5.11 풀이시간 5분 
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    min=sum(arr[0:4])
    max=sum(arr[1:])
    print(min,max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
