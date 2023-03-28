arr=[9,4,5,2,1,3,10]
n = len(arr)

def selectsort(depth):
    print(arr)
    if depth == n-1:
        return
    mi = arr[depth]
    idx = depth
    for i in range(depth+1,n):
        if mi > arr[i]:
            mi = arr[i]
            idx = i
    arr[depth] ,arr[idx] = arr[idx] , arr[depth]
    selectsort(depth+1)
selectsort(0)
