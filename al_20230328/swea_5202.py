


TC = int(input())
for T in range(1,TC+1):
    n = int(input())
    case = []
    for i in range(n):
        start,end = map(int,input().split())
        case.append((end,start))
    
    case.sort()
    time = 0
    res = 0
    for i in range(n):
        if time <= case[i][1]:
            time = case[i][0]
            res += 1
    print(f"#{T}", end=" ")
    print(res)