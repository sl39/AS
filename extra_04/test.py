import sys
sys.stdin = open("sample_input.txt")




TC = int(input())
for T in range(1,TC+1):
    n,m = map(int,input().split())
    mat = []
    for i in range(n):
        mat.append(list(input().strip()))
    water = []
    for i in range(n):
        for j in range(m):
            if mat[i][j] == "W":
                water.append([i,j])
    result = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == "L":
                cnt = m+n
                for k in water:
                    x,y = k
                    dis = abs(i-x) + abs(j-y)
                    if dis < cnt:
                        cnt = dis
                result += cnt
    print(f"#{T}",result)