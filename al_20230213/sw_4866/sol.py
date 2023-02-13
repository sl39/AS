import sys
sys.stdin = open("sample_input.txt")

TC = int(input())
for T in range(1,TC+1):
    stack = []
    ls = input().strip()
    cnt = 1
    for i in ls:
        if i == "(":
            stack.append(i)
        elif i == "{":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                cnt = 0
                break
        elif i == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                cnt = 0
                break
    if stack:
        print(f"#{T}",0)
    else:
        print(f"#{T}", cnt)