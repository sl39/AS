TC = int(input())


def dfs(i):
    stack = [i]
    arr[i] = 1
    while stack:
        node = stack.pop()
        for j in graph[node]:
            if not arr[j]:
                arr[j] = 1
                stack.append(j)

for T in range(1,TC+1):
    n,m = map(int,input().split())
    arr = [0] * (n+1)
    graph = [[] for i in range(n+1)]
    hmm = list(map(int,input().split()))
    for i in range(m):
        graph[hmm[2*i]].append(hmm[2*i+1])
        graph[hmm[2*i+1]].append(hmm[2*i])
    cnt = 0
    for i in range(1,n+1):
        if not arr[i]:
            dfs(i)
            cnt += 1
    
    print(f'#{T}', cnt)