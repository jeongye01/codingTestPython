#Simple Text Editor
# list.extend 대신 += 연산을 사용하였는데, +=는 객채를 새로 생성하기 때문에 훨씬 더 Cost가 높다는 점을 인지하게 되었다.
def simple_text_editor(queries):
    S = []
    job_history = []
    for query in queries:
        if 1 < len(query):
            query = query.split()
            if query[0] == '1':
                word = list(query[1])
                S.extend(word)
                job_history.append(('1', word))
            elif query[0] == '2':
                k = int(query[1])
                S, word = S[:-k], S[-k:]
                job_history.append(('2', word))
            else:
                k = int(query[1])
                print(S[k-1])
        else:
            query = job_history.pop()
            if query[0] == '1':
                k = len(query[1])
                S = S[:-k]
            else:
                word = query[1]
                S.extend(word)


Q = int(input())
queries = []
for _ in range(Q):
    queries.append(input())
simple_text_editor(queries)