# swea_5250

from heapq import heappop, heappush

TC = int(input())

dx = [1,-1,0,0]
dy = [0,0,-1,1]



for T in range(1,TC+1):
    mat = []
    n = int(input())
    for i in range(n):
        mat.append(list(map(int,input().split())))
    visited = [[1e9]*n for i in range(n)]
    
    q= []
    heappush(q,(0,0,0))
    while q:
        c , x, y = heappop(q)
        
        if visited[x][y] <= c:
            continue
        
        visited[x][y] = c
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n:
                if mat[x][y] <= mat[nx][ny]:
                    heappush(q,(c+ mat[nx][ny]-mat[x][y] + 1,nx,ny))
                else:
                    heappush(q,(c+1,nx,ny))
                           
    print(f'#{T}', end=" ")
    print(visited[n-1][n-1])