n, k = map(int, input().split())


def col(n, k):
    res = 0
    if k == 0:
        res += 1
        return res
    elif k > n:
        return 0
    else:
        res = col(n-1, k) + col(n-1, k-1)
        return res

print(col(n, k))
