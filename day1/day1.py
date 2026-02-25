


# 1. Printing to the screen
print("Hello, Python Learner!")

# 2. Variables
name = input("Enter your name: ")  # Input from user
age = input("Enter your age: ")

print(f"Hello {name}! You are {age} years old.")

# 3. Simple arithmetic
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "Undefined (cannot divide by 0)"

print(f"\nResults:")
print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {diff_result}")
print(f"{num1} * {num2} = {prod_result}")
print(f"{num1} / {num2} = {div_result}")

# 4. A simple conditional
if int(age) >= 18:
    print("You are an adult!")
else:
    print("You are not an adult yet.")
