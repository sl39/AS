import sys
sys.stdin = open("input.txt")

for T in range(1,11):
    n = int(input())
    sik = input().strip()
    stack = []
    res = []
    for i in sik:
        if i not in "+*":
            res.append(i)
        else:
            if i in "*":
                while stack and stack[-1] == "*":
                    res.append(stack.pop())
                stack.append(i)
            else:
                while stack and stack[-1] in "*+":
                    res.append(stack.pop())
                stack.append(i)


    while stack:
        res.append(stack.pop())

    stack1 = []
    for i in res:
        if i not in "*+":
            stack1.append(int(i))
        else:
            A = stack1.pop()
            B = stack1.pop()
            if i == "+":
                C = B+A
            else:
                C = B*A
            stack1.append(C)
    print(f"#{T}",stack1[0])


