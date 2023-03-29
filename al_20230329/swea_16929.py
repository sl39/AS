# # 1
# def quicksort(arr,left,right):
#     if left < right:
#         mid = cal(arr, left, right)
#         quicksort(arr,left,mid-1)
#         quicksort(arr,mid+1,right)

# def cal(arr,left,right):
#     i = left -1
#     j = left
#     pivot = arr[right]
#     while j < right:
#         if pivot > arr[j]:
#             i += 1
#             if i<j:
#                 arr[i], arr[j] = arr[j] , arr[i]    
#         j += 1
#     arr[i+1], arr[right] = arr[right] , arr[i+1]    
#     return i+1

# for i in range(3):
#     li = list(map(int,input().split()))
#     quicksort(li,0,len(li)-1)
#     print(*li)

# # 2
# def quick_sort(arr):
#     # 분할 정복
#     if len(arr) <= 1:
#         return arr
#     else:
#         # 분할 작업
#         pivot = arr[0]
#         left, right = [], []
#         for i in range(1, len(arr)):
#             if arr[i] > pivot:
#                 right.append(arr[i])
#             else:
#                 left.append(arr[i])
#         return [*quick_sort(left), pivot, *quick_sort(right)]


# nums = [55, 45, 23, 81, 28, 34, 60]
# print(quick_sort(nums))

# # 3 hoare partition 퀵정렬
def quick_sort(a, low, high):	# (리스트, 시작 인덱스, 끝 인덱스)
    if low < high:
        pivot = partition(a,low,high)
        quick_sort(a, low, pivot-1)
        quick_sort(a, pivot+1, high)
        
def partition(a, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    a[pivot], a[j] = a[j], a[pivot]
    return j

TC = int(input())
for T in range(1,TC+1):
    n = int(input())
    arr = list(map(int,input().split()))
    quick_sort(arr, 0, n-1)
    print(f'#{T}', end=" ")
    print(arr[n//2])