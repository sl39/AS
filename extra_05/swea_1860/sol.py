# import sys
# sys.stdin = open("input.txt")

TC = int(input())

for T in range(1,2):
    n,m,k = map(int,input().split())
    arr = list(map(int,input().split()))
    total_time = max(arr)
    time = [0]* (total_time+1)
    t = 0
    for i in arr:
        time[i] += 1

    t = 1
    point = 1
    bread = 0
    while t< total_time+1:
        if t%m == 0:
            bread += k
        if time[t]:
            bread -= time[t]
        if bread < 0:
            point = 0
            break
        t += 1

    print(f"#{T}", end=" ")
    if time[0]:
        print("Impossible")
    elif point:
        print("Possible")
    else:
        print("Impossible")
