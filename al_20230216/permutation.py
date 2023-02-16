p = list(range(1,10))
N = len(p)
key = 3

chosen = [1] * N

cnt = 0

def f(i, k, res):
    global cnt
    if i == k:
        print(res)
        cnt += 1
        return
    for j in range(N):
        if chosen[j]:
            chosen[j] = 0
            f(i+1,k,res+[p[j]])
            chosen[j] = 1

f(0,3,[])
print(cnt)
print(72*7)