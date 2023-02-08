import sys
sys.stdin = open("input.txt")

for T in range(1,11):
    stack = []
    N , newline = map(str,input().split())
    for i in newline:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    print(f"#{T}", "".join(stack))