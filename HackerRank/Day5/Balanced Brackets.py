#내 풀이->테스트 통과 DATE=>5.15 풀이시간20분
def isBalanced(s):
    # Write your code here
    type1Cnt=0
    type2Cnt=0
    type3Cnt=0
    opened=[]
    lastOpen=""
    for x in s:
        if x=="[":
            type1Cnt+=1
            opened.append("[")
        elif x=="{":
            type2Cnt+=1
            opened.append("{")
        elif x=="(":
            type3Cnt+=1
            opened.append("(")
        elif x=="]":
            if type1Cnt>0 and opened.pop()=="[":
                type1Cnt-=1
            else:
                return "NO"
        elif x=="}"  :
            if type2Cnt>0 and opened.pop()=="{":
                type2Cnt-=1
            else:
                return "NO"
        elif x==")" :
            if type3Cnt>0 and opened.pop()=="(":
                type3Cnt-=1
            else:
                return "NO"
    if type1Cnt==0 and type2Cnt==0 and type3Cnt==0:
        return "YES"
    else:
        return "NO"
            