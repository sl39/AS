## 중위 순회

import sys
sys.stdin = open("sample_input.txt")




TC = int(input())

def inorder(t = 1):
    global tree,i
    if t > n:
        return

    inorder(2*t)
    tree[t] = i
    i += 1
    inorder(2*t+1)



for T in range(1,2):
    i = 1
    n = int(input())
    tree = [0]*(n+1)
    inorder()
    print(f"#{T}", end=" ")
    print(tree[1], tree[n//2])
