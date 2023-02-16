import sys
sys.stdin = open("input1222.txt")

for T in range(1,11):
    n = int(input())
    ls = list(input().strip())
    stack = []
    result = []
    for i in ls:
        if i == "+":
            if stack:
                while stack:
                    result.append(stack.pop())
            stack.append(i)
        else:
            result.append(int(i))
    while stack:
        result.append(stack.pop())

    cal = []
    for i in result:
        if i == "+":
            a = cal.pop()
            b = cal.pop()
            cal.append(a+b)
        else:
            cal.append(i)
    print(f"#{T}", cal[0])