TC = int(input())

def find(i):
    stack = [i]
    while stack:
        node = stack.pop()
        if not arr[node]:
            arr[node] =i
            for j in graph[node]:
                stack.append(j)


for T in range(1,TC+1):
    n,m = map(int,input().split())
    arr = [0] * (n+1)
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1,n+1):
        if not arr[i]:
            find(i)
    
    print(f'#{T}', len(set(arr))-1)
