Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Simple calculator program
... 
... # Ask the user to input two numbers
... num1 = float(input("Enter the first number: "))
... num2 = float(input("Enter the second number: "))
... 
... # Ask the user to choose an operation
... operation = input("Choose an operation (+, -, *, /): ")
... 
... # Perform the selected operation
... if operation == '+':
...     result = num1 + num2
...     print(f"The result of {num1} + {num2} is {result}")
... elif operation == '-':
...     result = num1 - num2
...     print(f"The result of {num1} - {num2} is {result}")
... elif operation == '*':
...     result = num1 * num2
...     print(f"The result of {num1} * {num2} is {result}")
... elif operation == '/':
...     if num2 != 0:
...         result = num1 / num2
...         print(f"The result of {num1} / {num2} is {result}")
...     else:
...         print("Error: Division by zero is not allowed.")
... else:
...     print("Invalid operation. Please choose +, -, *, or /.")
