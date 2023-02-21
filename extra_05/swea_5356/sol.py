import sys
sys.stdin = open("sample_input.txt")

TC = int(input())

for T in range(1,TC+1):
    mat = []
    lenth = []
    for i in range(5):
        arr = list(input().strip())
        mat.append(arr)
        lenth.append(len(arr))

    ml = max(lenth)
    for i in range(5):
        for j in range(ml - lenth[i]):
            mat[i].append("")

    res = ''
    for i in range(ml):
        for j in range(5):
            res += mat[j][i]

    print(f'#{T}',res)
