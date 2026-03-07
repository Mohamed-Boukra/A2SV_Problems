def insertionSort1(n, arr):
    v = arr[-1]
    i = n - 1
    while i > 0 and arr[i-1] > v:
        arr[i] = arr[i-1]
        print(*arr)
        i -= 1
    arr[i] = v
    print(*arr)