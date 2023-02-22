import sys
sys.stdin = open("input.txt")

def inorder(k):
    if k > n:
        return
    inorder(k*2)
    print(arr[k][0],end = "")
    inorder(k*2+1)


for T in range(1,11):
    n = int(input())
    arr = [0] * (n+1)
    for i in range(n):
        ls = list(map(str,input().split()))
        arr[int(ls[0])] = ls[1:]
    print(f"#{T}", end= " ")
    inorder(1)
    print()


