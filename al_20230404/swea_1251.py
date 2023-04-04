
TC = int(input())

def find(a):
    if a != arr[a]:
        arr[a] = find(arr[a])
    return arr[a]

for T in range(1,TC+1):
    n = int(input())
    xarr = list(map(int,input().split()))
    yarr = list(map(int,input().split()))
    tex = float(input())
    res = []
    for i in range(n):
        for j in range(n):
            if i != j:
                res.append(((xarr[i]-xarr[j])**2 + (yarr[i]-yarr[j])**2,i,j))
    res.sort()
    arr = [i for i in range(n)]
    cost = 0
    for i in res:
        c,x,y = i
        xx = find(x)
        yy = find(y)
        if xx != yy:
            if xx > yy:
                arr[xx] = yy
            else:
                arr[yy] = xx
            
            cost += c
    print(f'#{T}', end =" ")
    print(round(cost*tex))