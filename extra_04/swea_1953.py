import sys
sys.stdin = open("sample_input.txt")


from collections import deque


delta =[0,
        [[0,0,1,-1],[1,-1,0,0]],
        [[1,-1],[0,0]],
        [[0,0],[1,-1]],
        [[-1,0],[0,1]],
        [[1,0],[0,1]],
        [[1,0],[0,-1]],
        [[-1,0],[0,-1]]]



TC = int(input())
for T in range(1, TC+1):
    cnt = 0
    n,m,r,c,l = map(int,input().split())
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))
    q = deque([[r,c]])
    location = [[0]* m for i in range(n)]
    location[r][c] = 1
    while q :
        r, c = q.popleft()
        if mat[r][c] == 1:
            dx,dy =delta[1]
            for i in range(4):
                nx = dx[i] + r
                ny = dy[i] + c
                if 0<= nx < n and 0<= ny < m and mat[nx][ny] and not location[nx][ny]:
                    location[nx][ny] = location[r][c] + 1

                    q.append([nx,ny])
        else:
            dx,dy =delta[mat[r][c]]
            for i in range(2):
                nx = dx[i] + r
                ny = dy[i] + c
                if 0<= nx < n and 0<= ny < m and mat[nx][ny] and not location[nx][ny]:
                    location[nx][ny] = location[r][c] + 1
                    q.append([nx,ny])
    cnt = 0
    for i in location:
        for j in i:
            if 0 < j<= l:
                cnt += 1
    print(f"#{T}",cnt)
    for i in location:
        print(i)
        