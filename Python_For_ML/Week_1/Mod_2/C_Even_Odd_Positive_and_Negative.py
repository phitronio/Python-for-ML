
n = int(input()) 

inp = input()

numbers= inp.split()

positive =0 ; negative =0 ; even =0 ; odd =0 


for i in range(n):
    x = int(numbers[i])
    # positive or negative
    if x > 0 :
        positive+=1 
    elif x < 0 :
        negative+=1 
    
    # odd or even
    if x % 2 !=0 :
        odd+=1 
    else:
        even+=1 


print("Even:",even)
print("Odd:",odd)
print("Positive:",positive)
print("Negative:",negative)