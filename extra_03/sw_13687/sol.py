import sys
sys.stdin = open("sample_input.txt")

TC = int(input())
for T in range(1,TC+1):
    N = int(input())
    mat = [0] * 401

    for i in range(N):
        now, home = map(int,input().split())
        if now > home:
            now , home = home , now
        if now %2 ==0:
            now -= 1
        if home %2 :
            home += 1
        for j in range(now,home+1):
            mat[j] += 1

    print(f"#{T}", max(mat))
