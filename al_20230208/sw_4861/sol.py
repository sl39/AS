import sys
sys.stdin = open("sample_input.txt")

TC = int(input())
for T in range(TC):
    N, M = map(int,input().split())
    mat = []
    for _ in range(N):
        mat.append(input().strip())
    cnt = 0
    mm = []

    for i in range(N):
        for j in range(N-M+1):
            mm = mat[i][j:j+M]
            if mm == mm[::-1]:
                cnt = 1
                break
        if cnt == 1:
            break

    new_mat = [[0]*N for i in range(N)]

    for i in range(N):
        for j in range(N):
            new_mat[i][j] = mat[j][i]

    print(f"#{T+1}", end = " ")
    if cnt:
        print(mm)
    else:
        for i in range(N):
            for j in range(N - M + 1):
                mm = new_mat[i][j:j+M]
                if mm == mm[::-1]:
                    cnt = 1
                    break
            if cnt == 1:
                break
        print("".join(mm))
