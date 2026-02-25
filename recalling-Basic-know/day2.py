# Day 2: Loops, Lists, and Conditionals

print("=== Day 2: Loops and Lists ===\n")

# 1. Lists
fruits = ["apple", "banana", "cherry", "date"]
print("My favorite fruits:", fruits)

# 2. Looping through a list
print("\nLooping through fruits:")
for fruit in fruits:
    print(fruit)

# 3. Using range() in a loop
print("\nNumbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# 4. While loop
print("\nCounting down from 5:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!\n")

# 5. Conditional inside a loop
print("Even numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        print(num)

# 6. Simple interactive program
names = []
print("\nEnter 3 names:")
for _ in range(3):
    n = input("Enter name: ")
    names.append(n)

print("Names you entered:", names)

