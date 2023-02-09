import sys
sys.stdin = open("input.txt")
## 회문
for T in range(10):
    N = int(input())
    mat = []
    for i in range(8):
        mat.append(input().strip())
    count = 0
    for i in range(8):

        for j in range(8-N+1):
            s1 = ""
            s2 = ""
            for k in range(N):
                s1 += mat[i][j+k]
                s2 += mat[j+k][i]

            if s1 == s1[::-1]:
                count += 1
            if s2 == s2[::-1]:
                count += 1
    print(f"#{T+1}",count)