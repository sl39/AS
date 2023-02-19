import sys
sys.stdin = open("sample_input.txt")

TC = int(input())
for T in range(1,TC+1):
    n,m = map(int,input().split())
    mat = [list(map(int,input().split())) for i in range(n)]
    t = 0
    houses = []
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                houses.append((i,j))
    
    t = 1
    myx = 1
    while t < 2*n:
        for i in range(n):
            for j in range(n):
                mx = 0
                for k in houses:
                    x,y = k
                    if abs(i-x) + abs(y-j) <= t:
                        mx += 1
                if mx*m >= (t+1)**2 + t**2:
                    myx = max(mx,myx)
        t += 1
    print(f"#{T}",myx)

