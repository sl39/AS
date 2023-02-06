# import sys
# sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    result = []
    numbers = list(map(int,input().split()))
    nl = len(numbers)
    for i in range(1<<nl):
        ls = []
        for j in range(nl):
            if i & (1<<j):
                ls.append(j)
        if sum(ls) == 2:
            result.append(ls)
    print(f"#{tc}", result)
