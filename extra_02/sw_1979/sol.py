import sys
sys.stdin = open("input.txt")

TC = int(input())
for T in range(1,TC+1):
    N , K = map(int,input().split())
    mat = []

    result = []
    cnt = 0
    for i in range(N):
        ls = list(map(int,input().split()))
        mat.append(ls)
    for i in mat:
        cnt = 0
        for j in i:
            if j == 1:
                cnt += 1
            else:
                result.append(cnt)
                cnt = 0
        result.append(cnt)
    cnt = 0
 
    for i in range(N):
        cnt = 0
        for j in range(N):
            if mat[j][i] == 1:
                cnt += 1
            else:
                result.append(cnt)
                cnt = 0
        result.append(cnt)
    res = 0
    for i in result:
        if i == K:
            res += 1
    print(f"#{T}",res)