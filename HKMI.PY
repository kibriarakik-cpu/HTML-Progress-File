def intro(name):
    print(f"Hello, {name}! Welcome to the HKMI Python module.")
    username = input("Please enter your username: ")
    intro(username)
def recur_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recur_factorial(n - 1)
    if num<0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num==0:
        print("The factorial of 0 is 1")
    else:
        print("The factorial of", num, "is", recur_factorial(num))
    def add_numbers(a, b):
        return a + b
    def subtract_numbers(a, b):
        return a - b
    def multiply_numbers(a, b):
        return a * b
    def divide_numbers(a, b):
        if b == 0:
            return "Error! Division by zero."
        else:
            return a / b
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice=input("Enter choice(1/2/3/4): ")
    print("The result is:", end=" ")
    if choice=='1':
        print(add_numbers(num1, num2))
    elif choice=='2':
        print(subtract_numbers(num1, num2))
    elif choice=='3':
        print(multiply_numbers(num1, num2))
    elif choice=='4':
        print(divide_numbers(num1, num2))
        