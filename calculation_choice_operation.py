# # print(input("Which type of operation do you want to perforrm?"))
# x= float(input("Enter value of a"))
# y= float(input("Enter value of b"))
# add =x+ y
# sub =x- y
# mul= x * y
# div= x/y
# modulus= x%y
# floor_div= x//y
# print(f"sum is: {add}, subtract is :{sub},  multiply is {mul}, divide is :{div}, modulus is: {modulus}, floor_div is: {floor_div}")
# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2 != 0:
    division = num1 / num2
    modulus = num1 % num2
else:
    division = "Undefined"
    modulus = "Undefined "

print("\nArithmetic Operations:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} % {num2} = {modulus}")
