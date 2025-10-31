
n = int(input())
arr = list(map(int, input().split()))

min_val = min(arr)
max_val = max(arr)

min_index = arr.index(min_val)
max_index = arr.index(max_val)

arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

print(*arr)