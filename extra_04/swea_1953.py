import sys
sys.stdin = open("sample_input.txt")


from collections import deque


delta = [0,
    [[1,-1,0,0],[0,0,1,-1]],
    [[1,-1],[0,0]],
    [[0,0],[1,-1]],
    [[-1,0],[0,1]],
    [[1,0],[0,1]],
    [[1,0],[0,-1]],
    [[-1,0],[0,-1]]]


TC = int(input())
for T in range(1,TC+1):
    
    cnt = 0
    n,m,r,c,l = map(int,input().split())
    mat = []
    for i in range(n):
        a = input().rstrip()
        a = a.replace(" ","0")
        mat.append(list(a))
        if i != n-1:
            mat.append(["0"]*(2*m-1))

    visited = [[-2]*(2*m-1) for i in range(2*n-1)]
    for i in range(2*n-1):
        for j in range(2*m - 1):
            if mat[i][j] == "1":
                visited[i][j] = 0
                dx, dy = delta[1]
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0<= nx < 2*n -1 and 0<= ny < 2*m -1:
                        if visited[nx][ny] == -2:
                            visited[nx][ny] = -1
                        elif visited[nx][ny] == -1:
                            visited[nx][ny] = 0
            elif mat[i][j] == "0":
                pass
            else:
                visited[i][j] = 0
                dx, dy = delta[int(mat[i][j])]
                for k in range(2):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0<= nx < 2*n -1 and 0<= ny < 2*m -1:
                        if visited[nx][ny] == -2:
                            visited[nx][ny] = -1
                        elif visited[nx][ny] == -1:
                            visited[nx][ny] = 0
    cnt = 1
    r = 2*r 
    c = 2*c
    visited[r][c] = 1
    q = deque([[r,c]])
    dx, dy = delta[1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx < 2*n -1 and 0<= ny < 2*m - 1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    if visited[nx][ny] % 2:
                        cnt += 1
                    if visited[nx][ny] == 2*l - 1:
                        pass
                    else:
                        q.append((nx,ny))
    if l == 1:
        print(f"#{T}",1)
    else:
        print(f"#{T}",cnt)



