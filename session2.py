
# Create two whole-number variables and display their types.
a = 15
b = 12

print("Type of a:", type(a))
print("Type of b:", type(b))
# Calculate and display the four arithmetic results.
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Convert the division result to an integer, then to a float.
c = int(a / b)
print("Value of c:", c)
print("Type of c:", type(c))

c = float(c)
print("New value of c:", c)
print("New type of c:", type(c))
# Convert c to text and join it with the message
message = "The result of a divided by b is "
print(message + str(c))
# Compare a and b; each comparison gives True or False.
print("Is a greater than b?", a > b)
print("Is a equal to b?", a == b)