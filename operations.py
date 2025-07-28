# Input two values from the user
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

print( "Arithmetic Operations" )
print(f"sum = {a + b}")
print(f"subtract = {a - b}")
print(f" multiply = {a * b}")
print(f"divide = {a / b if b != 0 else 'Undefined'}")
print(f"modulus = {a % b if b != 0 else 'Undefined'}")
print(f"power = {a ** b}")
print(f"floor_div = {a // b if b != 0 else 'Undefined'}")



print("Assignment Operations" )
x = a
x += b
print(f"x += b{x}")
x = a
x -= b
print(f"x -= b{x}")
x = a
x *= b
print(f"x *= b{x}")
x = a
x = x / b if b != 0 else "Undefined"
print(f"x /= b{x}")

print("Comparison Operations")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")

print(f"a <= b: {a <= b}")
