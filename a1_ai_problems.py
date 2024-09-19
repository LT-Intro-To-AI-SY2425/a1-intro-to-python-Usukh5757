# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

# First problem is to make a simple calculator that can do addition, subtraction, division, and multiplication

def simple_calc():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Error: Invalid operation."

    return f"Result: {result}"

print(simple_calc())

# Second problem is to determine if a given number is even or odd.

def evenorodd():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

print(evenorodd())

# The third problem is to count how many vowels a word has

def countvowels():
    vowels = "aeiouAEIOU"
    user_input = input("Enter a string: ")
    count = sum(1 for char in user_input if char in vowels)
    return f"Number of vowels: {count}"
print(countvowels())