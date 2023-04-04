# swea_5251

from heapq import heappop, heappush

TC = int(input())

for T in range(1,TC+1):
    n,m = map(int,input().split())
    graph = [[] for i in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((c,b))
        
    visited =[1e9]*(n+1)
    q = []
    heappush(q,(0,0))
    
    while q:
        cost , x= heappop(q)
        
        if cost >= visited[x]:
            continue
        
        visited[x] = cost
        for i in graph[x]:
            c, next = i
            heappush(q,(c+cost,next))
            
    
    print(f'#{T}', end = " ")
    print(visited[n])