T = int(input())
 
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    # 2 2 2
    # 3 4
    fish = 0
    time = 0
    idx = 0
    result = "Possible"
    while time <= max(arr):
        if time != 0 and not time % M:
            fish += K
        if arr[idx] == time:
            if fish > 0:
                fish -= 1
                idx += 1
            else:
                result = "Impossible"
                break
        time += 1
 
    print(f'#{tc} {result}')