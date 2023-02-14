import sys
sys.stdin = open("input.txt")

for T in range(1,11):
    a, n = map(int,input().split())
    nums = list(map(int,input().split()))
    mat = [[0] *100 for i in range(100)]
    for i in range(n):
        mat[nums[2*i]][nums[2*i+1]] = 1
    stack = [0]
    cnt = 0
    while stack:
        p = stack.pop()
        if p == 99:
            cnt = 1
            break
        for i in range(100):
            if mat[p][i]:
                mat[p][i] = 0
                stack.append(i)
    print(f"#{T}",cnt)






