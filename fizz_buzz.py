# Set initial value to start at
num = 0

# Loop through each number from 1 to 100
while num <= 100:
    # Check if number is divisible for printing other values
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")       # Prints FizzBuzz if divisible by 3 and 5
    elif num % 3 == 0:
        print("Fizz")           # Prints Fizz if divisible by 3
    elif num % 5 == 0:
        print("Buzz")           # Prints Buzz if divisible by 5
    else:
        print(num)              # Prints the number if not divisible by 3 or 5
    num += 1