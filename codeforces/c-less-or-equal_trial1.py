n, k = map(int, input().split())
a = sorted(map(int, input().split()))

if k == 0:
    x = a[0] - 1
    print(x if x >= 1 else -1)
elif k == n:
    print(a[n-1])
else:
    x = a[k-1]
    if a[k] == x:
        print(-1)
    else:
        print(x)