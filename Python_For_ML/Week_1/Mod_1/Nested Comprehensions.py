# --- DEMO: Nested Comprehensions and Conditional Logic ---
# Create a list of lists where inner lists contain squares of even numbers
nested_squares = [[x**2 for x in range(i, i+5) if x % 2 == 0] for i in range(1, 10, 3)]
print("Nested Squares:", nested_squares)

# Create a dictionary mapping numbers to a description based on conditions
number_descriptions = {
    num: ("Even and divisible by 3" if num % 2 == 0 and num % 3 == 0
          else "Even" if num % 2 == 0
          else "Odd and divisible by 3" if num % 3 == 0
          else "Odd")
    for num in range(1, 100)
}
print("Number Descriptions:", number_descriptions)