def binary(i,start,end,a,b):
    mid = (start+end)//2
    if start > end:
        return 0 
    if i == arr[mid]:
        return 1 
    if i > arr[mid]:
        if a == 1:
            return 0
        return binary(i,mid+1,end,1,0)
    if i < arr[mid]:
        if b == 1:
            return 0
        return binary(i,start,mid-1,0,1)

TC = int(input())
for T in range(1,TC+1):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    sea = list(map(int,input().split()))
    ans = 0
    for i in sea:
        ans += binary(i,0,n-1,0,0)
    print(f'#{T}', end=" ")
    print(ans)