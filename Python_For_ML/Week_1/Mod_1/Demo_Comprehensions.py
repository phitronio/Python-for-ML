# --- DEMO: Comprehensions ---
temp = [35, 40, 28, 32, 30]

farhen = [item*(9/5)+32 for item in temp]
print(f"First {farhen}")

farhen1 = [item*(9/5)+32 for item in temp if item % 2 == 0]
print(farhen1)

for item in temp:
  print(item*(9/5)+32)

squares = [x**2 for x in range(6)]

evens = [x for x in range(20) if x % 2 == 0]

square_map = {x: x**2 for x in range(5)}

unique_initials = {item[0].lower() for item in ["Alice", "Bob", "alex", "Beta"]}

print(f"Square is : {squares}")
print(f"even: {evens}")
print(f"smap: {square_map}")
print(f"ui : {unique_initials}")