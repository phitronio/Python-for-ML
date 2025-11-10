from functools import reduce

def find_average(arr):
    total = reduce(lambda x, y: x+y, arr)
    return total / len(arr)

n = int(input())
A = list(map(float, input().split()))

average = find_average(A)

print(f"{average:.7f}")