from heapq import heappop,heappush

TC = int(input())


dx= [1,-1,0,0]
dy = [0,0,-1,1]

for T in range(1,TC+1):
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int,list(input().strip()))))
    visited = [[1e9] *n for i in range(n)]
    
    q = []
    heappush(q,(0,0,0))
    
    while q:
        cost,x,y = heappop(q)
        
        if visited[x][y] <= cost:
            continue
        
        visited[x][y] = cost
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx< n and 0<= ny < n:
                heappush(q,(cost+mat[nx][ny],nx,ny))
    
    print(f'#{T}', visited[-1][-1])