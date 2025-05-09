num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: +, -, *, /")
op = input("Operation: ")

if op == '+':
    result = num1 + num2
    print("Result:", result)
elif op == '-':
    result = num1 - num2
    print("Result:", result)
elif op == '*':
    result = num1 * num2
    print("Result:", result)
elif op == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operator")
