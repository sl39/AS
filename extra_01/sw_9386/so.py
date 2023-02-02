import sys
sys.stdin = open("input1.txt")

T = int(input())
for i in range(1,T+1):
    N = int(input())
    ls = input().strip()
    maxx = 0
    cnt = 0
    for j in ls:
        if j == "1":
            cnt += 1
        else:
            maxx = max(cnt,maxx)
            cnt = 0
    maxx = max(cnt,maxx)
    print(f"{i}", maxx)
