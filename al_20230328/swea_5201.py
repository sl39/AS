TC = int(input())
for T in range(1,TC+1):
    n,m = map(int,input().split())
    container = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    truck.sort(reverse=True)
    weight = [0] * 101
    res = 0
    
    for i in container:
        weight[i] += 1

    
    for i in truck:
        for j in range(100,-1,-1):
            if weight[j] and i >= j:
                res += j
                weight[j] -= 1
                break
    print(f"#{T}", end=" ")
    print(res)