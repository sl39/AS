import sys
sys.stdin = open("input.txt")

TC = int(input())

for i in range(1,TC + 1):
    s = int(input())
    carrot = list(map(int,input().split()))
    result = [1]
    for j in range(1,s):
        if carrot[j] > carrot[j-1]:
            result.append(result[-1]+1)
        else:
            result.append(1)
    print(f"#{i}",max(result))