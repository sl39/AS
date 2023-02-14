import sys
sys.stdin = open("sample_input.txt")

TC = int(input())

for T in range(1, TC+1):
    V, E = map(int, input().split())
    mat = [[0] * (V+1) for i in range(V+1)]
    for i in range(E):
        p, c = map(int, input().split())
        mat[p][c] = 1
    S, G = map(int, input().split())
    stack = [S]
    cnt = 0
    while stack:
        po = stack.pop()
        if po == G:
            cnt = 1
            break
        for i in range(V+1):
            if mat[po][i]:
                stack.append(i)
                mat[po][i] = 0
    print(f'#{T}',cnt)

