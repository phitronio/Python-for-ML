def new_array(A, B):
    return B +A
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C= new_array(A , B)

print(*C)