import sys
sys.stdin = open("input.txt")

TC = int(input())
for T in range(1,TC+1):
    N,M = map(int,input().split())
    dx = [i for i in range(M)]
    dy = [i for i in range(M)]
    mat = [list(map(int,input().split())) for i in range(N)]
    mys = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            my = 0
            for k in dx:
                nx = k +i
                for l in dy:
                    ny = l + j
                    my += mat[nx][ny]
                mys = max(mys,my)
    print(mys)

            
