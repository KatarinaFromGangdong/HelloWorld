# simple calculator using if-else statement

operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1+num2
elif operator == "-":
    result = num1-num2
elif operator == "*":
    result = num1*num2
elif operator == "/":
    if num2 != 0:
        result = num1/num2
    else: 
        print("Math Error")
elif operator == int():
    print("Invalid operator")
else:
    print("Syntax Error")
    
print(f"The result of {num1} and {num2} is {result}.")