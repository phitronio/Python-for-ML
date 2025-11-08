sum = 0

for i in range(1,11):

    print(i, "is pricessing");

    if i % 2 ==0 :
        continue;
    
    sum+= i
    print(i, "sum");

####

accuricy = 90 
for i in range(100):
    accuricy+=1
    print(accuricy);
    if accuricy == 100:
       break


changed_or_not = True

while True:
    if changed_or_not == False and accuricy == 100:
        break

    if (prev>accuricy):
        changed_or_not = False