import sys
sys.stdin = open("input1224.txt")

for T in range(1,11):
    n = int(input())
    ls = input().strip()
    result = []
    stack = []
    for i in ls:
        if i not in "(+*)":
            result.append(i)
        elif i == "(":
            stack.append(i)
        elif i == "*":
            if stack and stack[-1] == "*":
                while stack and stack[-1] == "*":
                    result.append(stack.pop())
            stack.append(i)
        elif i == "+":
            if stack and stack[-1] in "*+":
                while stack and stack[-1] in "*+":
                    result.append(stack.pop())
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()
    while stack:
        result.append(stack.pop())

    mys = 0

    stack1 = []
    for i in result:
        if i not in "*+":
            stack1.append(int(i))
        else:
            a = stack1.pop()
            b = stack1.pop()
            if i == "*":
                c = b * a
            else:
                c = b + a
            stack1.append(c)

    print(f"#{T}",stack1[0])