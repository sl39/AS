def find(p):
    if p != arr[p]:
        arr[p] = find(arr[p])
    return arr[p]

TC = int(input())
for T in range(1,TC+1):
    n,m  = map(int,input().split())
    
    arr = [i for i in range(n+1)]
    graph = []
    for i in range(m):
        graph.append(list(map(int,input().split())))
    graph= sorted(graph,key=lambda x: x[2])
    cost = 0

    for i in graph:
        x,y, c = i
        pp = find(x)
        qq = find(y)
        
        if pp != qq:
            if pp < qq:
                arr[pp] = arr[qq]
            else:
                arr[qq] = arr[pp]
            cost += c

    print(f'#{T}', end=" ")
    print(cost)