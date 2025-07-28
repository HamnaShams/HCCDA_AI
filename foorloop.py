#print table 1 to 10
for num in range(1,11):
    print(f"table of:{num}")
    for i in range(1,11):
        print(f" {num} * {i}= {num*i}")
        
#print desired table
num= int(input("Enter a number whose table you want to print"))
print(f"Printing table of:{num}")
for i in range(1,11):
    print(f" {num} * {i}= {num*i}")
