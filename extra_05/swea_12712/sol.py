import sys
sys.stdin = open("in1.txt")

TC = int(input())
for T in range(1,TC+1):
    n, m = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(n)]

    dx = []
    dy = []
    for i in range(1,m):
        dx += [i,i,-i,-i,0,-i,0,i]
        dy += [0,i,0,-i,i,i,-i,-i]

    myx = 0
    for i in range(n):
        for j in range(n):
            my1 = mat[i][j]
            my2 = mat[i][j]
            for k in range(8*(m-1)):
                nx = dx[k] + i
                ny = dy[k] + j
                if 0<= nx <n and 0<= ny < n:
                    if k %2:
                        my1 += mat[nx][ny]
                    else:
                        my2 += mat[nx][ny]
            myx = max(my1,my2,myx)
    print(f"#{T}",myx)