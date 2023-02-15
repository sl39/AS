import sys
sys.stdin = open("sample_input.txt")

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(v):
    global mat, cnt
    for i in range(4):
        nx = dx[i] + v[0]
        ny = dy[i] + v[1]
        if 0 <= nx < n and 0 <= ny < n:
            if mat[nx][ny] == "3":
                cnt = 1
                return
            elif mat[nx][ny] == "0":
                mat[nx][ny] = "1"
                dfs([nx,ny])


TC = int(input())
for T in range(1,TC+1):
    n = int(input())

    mat = []
    for i in range(n):
        mat.append(list(input().strip()))
    for i in range(n):
        for j in range(n):
            if mat[i][j] == "2":
                v = [i, j]
                break

    cnt = 0
    dfs(v)
    print(f"#{T}",cnt)


