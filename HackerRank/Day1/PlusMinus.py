#내 풀이->테스트 통과 DATE=>5.11 풀이시간 5분 

def plusMinus(arr):
    pn,zn,mn=0,0,0
    for a in arr:
        if a>0:
            pn+=1
        elif a==0:
            zn+=1
        else:
            mn+=1
    length=len(arr)
    print(format(pn/length,".6f"))
    print(format(mn/length,".6f"))
    print(format(zn/length,".6f"))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)