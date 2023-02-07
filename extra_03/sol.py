import sys
sys.stdin = open("input1.txt")

TC = int(input())
for T in range(TC):
    mat = []
    N , M= map(int,input().split())
    result = []
    for i in range(N):
        mat.append(list(map(int,input().split())))

    for i in range(N):
        mys = 0
        for j in range(M):
            if mat[i][j] == 1:
                mys += 1
            else:
                result.append(mys)
                mys = 0
            if j == N-1:
                result.append(mys)

    for i in range(M):
        mys = 0
        for j in range(N):
            if mat[j][i] == 1:
                mys += 1
            else:
                result.append(mys)
                mys = 0
            if j == M-1:
                result.append(mys)
    print(f'#{T+1}',max(result))