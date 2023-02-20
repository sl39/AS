# def f(i, k):
#     if i == k:
#         print(bit)
#     else:
#         bit[i] = 1
#         f(i+1,k)
#         bit[i] = 0
#         f(i+1,k)

# A = list(range(1,11))
# N = len(A)
#
# bit = [0]*N
# f(0, 2)

# def f(i, k, key):
#     if i == k:
#         s = 0
#         for j in range(k):
#             if bit[j]:
#                 s += A[j]
#         if s == key:
#             return 1
#         return 0
        # if s == key:
        #     for j in range(k):
        #         if bit[j]:
        #             print(A[j], end=" ")
        #     print()

#     else:
#         bit[i] = 1
#         if f(i+1, k, key):
#             return 1
#         bit[i] = 0
#         if f(i+1, k, key):
#             return 1
#         return 0
#
# print(f(0,N,10) )



k , m = map(int,input().split())

A = list(range(1,k+1))
com = []

def f(i,s,m): # i: 원소, s: i-1까지 고려된 리스트, m: 원하는 원소의 개수
    global com
    if len(s) == m:
        com.append(s)
        return
    if k == i:
        return
    f(i+1, s+[A[i]],m)        # A[i] 포함
    f(i+1, s,m)             # A[i] 미포함

f(0,[],m)
print(com)





# N = 10

# res = []
# fcnt  = 0
# def f(i,k,s,mys,key):
#     global res, fcnt
#     fcnt += 1
#     if mys == key:
#         res.append(s)
#         return
#     if mys > key:
#         return
#     if i == k:
#         return
#     f(i+1,k,s+[A[i]],mys+A[i],key)
#     f(i+1,k,s,mys,key)

# f(0,N,[],0,10)
# print(res,fcnt)
#


# def f(i,k,s,n):
#     if k == n:
#         print(s)
#         return
#     if i == N:
#         return

#     f(i+1,k,s+[A[i]],n+1)
#     f(i+1,k,s,n)

# f(0,4,[],0)