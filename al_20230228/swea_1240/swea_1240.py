import sys
sys.stdin = open("input.txt")

TC = int(input())
sc = ["0001101","0011001","0010011","0111101","0100011","0110001","0101111","0111011","0110111","0001011"]


# 홀수자리합*3 + 짝수자리의 합 == 10의배수
for T in range(1,TC+1):
    n,m = map(int,input().split())
    mat = []
    for i in range(n):
        mat.append(list(input().strip()))
    cnt = 0
    for i in range(n):
        for j in range(m-1,-1,-1):
            if mat[i][j] == "1":
                cnt = 1
                break
        if cnt:
            break
    code = mat[i][j-55:j+1]
    result = []
    for i in range(8):
        ac = "".join(code[i*7:(i+1)*7])
        for j in range(10):
            if ac == sc[j]:
                result.append(j)
                break
    value = 0
    for i in range(8):
        if i %2 == 0:
            value += result[i]*3
        else:
            value += result[i]
    print(f"#{T}", end=" ")
    if value % 10 == 0:
        print(sum(result))
    else:
        print(0)



