import sys
sys.stdin = open("input1.txt")

TC = int(input())
for T in range(1,TC+1):
    N, M = map(int,input().split())
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))
    dx = [1,-1,0,0,0]
    dy = [0,0,-1,1,0]
    my_max = 0
    for i in range(N):
        for j in range(M):
            val = 0
            for k in range(5):
                nx = dx[k] + i
                ny = dy[k] + j
                if 0<= nx < N and 0<= ny < M:
                    val += mat[nx][ny]
            if my_max < val:
                my_max = val
    print(f"{T}",my_max)