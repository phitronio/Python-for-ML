t = int(input())

for i in range(t):
    number = int (input())
    if number ==0 :
        print(0)
        continue
    while number > 0 :
        print(number%10, end=" ")
        number//=10
    print()