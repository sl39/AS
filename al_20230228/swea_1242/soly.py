import sys
sys.stdin = open("sample_input (1).txt")


dic1 = {"0001101":0,
        "0011001":1,
        "0010011":2,
        "0111101":3,
        "0100011":4,
        "0110001":5,
        "0101111":6,
        "0111011":7,
        "0110111":8,
        "0001011":9}



TC = int(input())
for T in range(1,TC+1):
    n,m = map(int,input().split())
    mat = []
    for i in range(n):
        mat.append(list(input().strip()))


    result = []
    for i in range(n):
        k = 0
        for j in range(m):
            if mat[i][j] != "0":
                k += 1
            elif mat[i][j] == "0":
                if mat[i][j-k:j] not in result and len(mat[i][j-k:j]) >= 14 and (len(mat[i][j-k:j])%14 == 0 or len(mat[i][j-k:j])%14==1):
                    result.append(mat[i][j-k:j])
                k = 0

    print(result)
    # arr = []
    # for i in result:
    #     v = "0000"
    #     for j in i:
    #         a = bin((int(j,16)))[2:]
    #         v += "0" * (4-len(a)) + a
    #     for j in range(len(v)):
    #         if v[-j] == "1":
    #             break
    #     arr.append(v[:-j+1])
    # print(arr)
    # res = 0
    # for i in arr:
    #     cal = []
    #     if len(i) // 56 == 1:
    #         cal.append(dic1[arr[0][-7:]])
    #         for j in range(1,8):
    #             cal.append(dic1[i[-7*j - 7:-j*7]])
    #         total = 0
    #         for j in range(8):
    #             if j %2 == 0:
    #                 total += cal[j]
    #             else:
    #                 total += 3 * cal[j]
    #         if total %10 ==0:
    #             res += sum(cal)
    #     elif len(i) // 56 == 2:
    #         cal.append(dic1[arr[0][-14::2]])
    #         for j in range(1, 8):
    #             cal.append(dic1[i[-14 * j - 14:-j * 14:2]])
    #         total = 0
    #         for j in range(8):
    #             if j % 2 == 0:
    #                 total += cal[j]
    #             else:
    #                 total += 3 * cal[j]
    #         if total % 10 == 0:
    #             res += sum(cal)
    #
    #
    # print(res)

