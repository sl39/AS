import sys
sys.stdin = open("input2.txt")

dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

TC = int(input())
for T in range(1,TC+1):
    n,m = map(int,input().split())
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))
    possible = 0
    for i in range(n):
        for j in range(m):
            cnt = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and mat[i][j] > mat[nx][ny]:
                    cnt += 1
            if cnt >= 4:
                possible += 1
    print(f"#{T}",possible)