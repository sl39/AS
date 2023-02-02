import sys
sys.stdin = open("input.txt")

for k in range(1, 11):
    flatten_try = int(input())
    height = list(map(int, input().split()))


    for i in range(flatten_try):
        idx_max = 0
        idx_min = 0
        result_max = height[0]
        for num in range(1, len(height)):
            if result_max < height[num]:
                result_max = height[num]
                idx_max = num
        height[idx_max] -= 1

        result_min = height[0]
        for num in range(1, len(height)):
            if result_min > height[num]:
                result_min = height[num]
                idx_min = num
        height[idx_min] += 1
    
    result_max = 0
    for num in range(1, len(height)):
        if result_max < height[num]:
            result_max = height[num]


    
    result_min = 100
    result_min = height[0]
    for num in range(1, len(height)):
        if result_min > height[num]:
            result_min = height[num]


    print(result_max - result_min)