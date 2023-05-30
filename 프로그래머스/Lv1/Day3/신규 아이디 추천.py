#https://school.programmers.co.kr/learn/courses/30/lessons/72410
###내 풀이->테스트 통과 DATE=>5.29 풀이시간 25분 
def solution(new_id):
    new_id=new_id.lower()
    for x in new_id:
        if not (ord('a')<=ord(x)<=ord('z') or ord('0')<=ord(x)<=ord('9') or x in ['-','_','.']):
            new_id=new_id.replace(x,'')
    new_id=new_id.split('.')
    tmp=[]
    for i in new_id:
        if i!='':
            tmp.append(i)
    new_id=".".join(tmp)
    if new_id=='':
        new_id='a'
    new_id=new_id[0:15]
    if new_id[-1]=='.':
        new_id=new_id[0:-1]
    if len(new_id)<=2:
        new_id+=new_id[-1]*(3-len(new_id))

    return new_id