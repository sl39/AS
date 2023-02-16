import sys
sys.stdin = open("sample_input.txt")

def permutation(i,n,s):
    global chosen, myx
    if s >= myx:
        return
    if i == n:
        if s < myx:
            myx = s
        return
    for j in range(n):
        if chosen[j]:
            chosen[j] = 0
            permutation(i+1,n,s+mat[i][j])
            chosen[j] = 1




TC = int(input())

for T in range(1, 1+TC):
    n = int(input())
    mat = []
    chosen = [1] * n
    myx = 100
    for i in range(n):
        mat.append(list(map(int,input().split())))
    permutation(0, n, 0)
    print(f"#{T}",myx)