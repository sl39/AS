TC = int(input())
for _ in range(TC):
    arr = [0] * 10
    a = input().strip()
    for i in a:
        arr[int(i)] += 1
    
    cnt = 0
    for i in range(10):
        if arr[i] and arr[i] //3:
            cnt += arr[i]//3
            arr[i] -= (arr[i]//3)*3
            
        if i>=2 and arr[i] and arr[i-1] and arr[i-2]:
            while arr[i]:
                arr[i] -= 1
                arr[i-1] -= 1
                arr[i-2] -= 1
                cnt += 1
    if cnt == 2:
        print(True)
    else:
        print(False)