n = int(input())
arr = list(map(int, input().split()))

lowest = min(arr)

position = arr.index(lowest) + 1

print(lowest, position)