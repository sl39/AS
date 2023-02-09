import sys
sys.stdin = open("input.txt")

for T in range(1,11):
    input()
    mat = []
    for i in range(100):
        mat.append(input().strip())
    cnt = 0
    new_mat = [[0]* 100 for i in range(100)]
    for i in range(100):
        for j in range(100):
            new_mat[i][j] = mat[j][i]

    for j in range(99):
        for i in range(100):
            for k in range(j+1):
                if mat[i][k:100-j+k] == mat[i][k:100-j+k][::-1]:
                    cnt = 100-j
                    break
                if new_mat[i][k:100-j+k] == new_mat[i][k:100-j+k][::-1]:
                    cnt = 100-j
                    break
            if cnt:
                break
        if cnt:
            break
    
    print(f"#{T}",cnt)