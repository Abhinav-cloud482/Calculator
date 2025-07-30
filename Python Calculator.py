#Python Calculator

operator = input("Enter an operator (+, -, *, /) :  ")
num1 = float(input("Enter the 1st number :  "))
num2 = float(input(" Enter the 2nd number :  "))

#print(num1 + num2)

if operator == " + ":
    result = num1 + num2
    print("result : {result}")
elif operator == " - ":
    result = num1 - num2
    print("result : {result}")
elif operator == "*":
    result = num1 * num2
    print("result : {result}")
elif operator == "/":
    result = num1 / num2
    print("result : {result}") 
else:
    print(f"{operator} is not valid")
