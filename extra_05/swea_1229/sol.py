import sys
sys.stdin = open("input (1).txt")

for T in range(1,11):
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))
    # 1 = N
    # 2 = S
    cnt = 0
    for i in range(n):
        stack = []
        for j in range(n):
            if stack and mat[j][i] == 2:
                stack.append(2)
            elif mat[j][i] == 1:
                stack.append(1)
        while stack and stack[-1] == 1:
            stack.pop()
        point = 0
        for k in range(len(stack)):
            if stack[k] == 1 and point ==0:
                point = 1
            elif stack[k] == 2 and point == 1:
                point = 0
                cnt += 1
    print(f"#{T}", cnt)
