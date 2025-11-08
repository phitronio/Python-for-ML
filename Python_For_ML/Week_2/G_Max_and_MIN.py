def find_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]

    for x in arr:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x

    return min_val, max_val

n = int(input())
A = list(map(int, input().split()))

mn, mx = find_min_max(A)
print(mn,mx)
