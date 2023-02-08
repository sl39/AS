import sys
sys.stdin = open("input.txt")
f = ["*","+","(",")"]
for t in range(1,11):
    N = int(input())
    ls = input().strip()
    stack = []
    for i in range(N):
        if ls[i] not in f:
            if i != 0:
                if ls[i-1] == "*":
                    pass
                else:
                    stack.append(int(ls[i]))
            else:
                stack.append(int(ls[i]))

        elif ls[i] == "*":
            if ls[i+1] != "(":
                p = stack.pop()
                stack.append(p*int(ls[i+1]))
            else:
                stack.append("*")
        elif ls[i] == "(":
            stack.append("(")
        elif ls[i] == ")":
            mys = 0
            while stack[-1] != "(":
                mys += stack.pop()
            stack.pop()
            if stack:
                if stack[-1] == "*":
                    stack.pop()
                    mys *= stack.pop()
            stack.append(mys)
    print(f"#{t}",sum(stack))
