import sys

data = sys.stdin.read().split()

if data:
    n = int(data[0])
    t = int(data[1])
    a = list(map(int, data[2:]))

    left = 0
    current_sum = 0
    ans = 0

    for right in range(n):
        current_sum += a[right]
        
        while current_sum > t:
            current_sum -= a[left]
            left += 1
        current_count = right - left + 1
        if current_count > ans:
            ans = current_count
    sys.stdout.write(str(ans) + '\n')