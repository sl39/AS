T = int(input())
for _ in range(T):
    arr = input()
    arr = sorted(arr)
    li = []
    result = ''
    visited = [0 for _ in range(6)]

    for i in range(4):
        if arr[i] == arr[i + 1] == arr[i + 2]:
            li.append(arr[i])
            li.append(arr[i+1])
            li.append(arr[i+2])
            visited[i] += 1
            visited[i+1] += 1
            visited[i+2] += 1
    for i in range(4):
        if visited[i] == 0:
            if int(arr[i + 2]) - int(arr[i+1]) == 1 and int(arr[i+1]) - int(arr[i]) == 1:
                li.append(arr[i])
                li.append(arr[i+1])
                li.append(arr[i+2])
                visited[i] += 1
                visited[i+1] += 1
                visited[i+2] += 1


    if len(li) == 6:
        print(True)
    else:
        print(False)