#SIMPLE CALCULATOR

print("Welcome to Simple Calculator!!")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def modulus(x, y):
    if y == 0:
        return "Error! Modulus by zero."
    else:
        return x % y

def calculator():
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '1':
        print("Addition of Numbers is:", add(num1, num2))
    elif choice == '2':
        print("subtraction of Numbers is:", subtract(num1, num2))
    elif choice == '3':
        print("Multiplication of Numbers is:", multiply(num1, num2))
    elif choice == '4':
        print("Division of Numbers is:", divide(num1, num2))
    elif choice == '5':
        print("Modulus of Numbers is:", modulus(num1, num2))
    else:
        print("Invalid input")
        
calculator()
