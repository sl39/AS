def merge_sort(arr):
    global cnt
    if len(arr)< 2:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    qwe = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            qwe.append(left[i])
            i += 1
        else:
            qwe.append(right[j])
            j += 1
    if left[-1] > right[-1]:
        cnt += 1
    qwe += left[i:]
    qwe += right[j:]
    return qwe

TC = int(input())

for T in range(1,TC+1):
    n = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print(f'#{T}',arr[n//2], cnt)