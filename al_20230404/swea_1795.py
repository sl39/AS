from heapq import heappop, heappush

TC = int(input())

def find(i,end):
    visited= [1e9] * (n+1)
    q = []
    heappush(q,(0,i))
    while q:
        c , start = heappop(q)
        if c >= visited[start]:
            continue
        visited[start] = c
        if i != end and start == end:
            arr[i] = visited[end]
            return
        for j in graph[start]:
            heappush(q,(j[0]+c,j[1]))
    
    return visited


for T in range(1,TC+1):
    n,m,end = map(int,input().split())
    
    arr = [0] * (n+1)
    
    graph = [[] for i in range(n+1)]
    
    for i in range(m):
        s,e,c = map(int,input().split())
        graph[s].append((c,e))
    
    for i in range(1,n+1):
        if i == end:
            vi = find(i,end)
        else:
            find(i,end)
    mx = 0
    for i in range(1,n+1):
        cnt = arr[i]+ vi[i]
        mx = max(cnt,mx)
    print(f"#{T}", mx)
    