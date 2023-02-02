import sys
sys.stdin = open("input.txt")

for i in range(1, 11):
    num = int(input())
    ls = list(map(int,input().split()))
    lenth = len(ls)
 
    while num > 0:
        M = 0
        Mj = 0
        m = 100
        mj = 0
        for j in range(lenth):
            if ls[j] > M:
                M = ls[j]
                Mj = j
 
            if ls[j] < m:
                m = ls[j]
                mj = j
        if m == M:
            break
        else:
            ls[Mj] -= 1
            ls[mj] += 1
        num -= 1
    maxx = 0
    mini = 100
    for j in ls:
        if maxx < j:
            maxx = j
        if mini > j:
            mini = j
    print(f"#{i}",maxx- mini)