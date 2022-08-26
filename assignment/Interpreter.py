num1=input("Enter a number: ")
operator=input("Enter your preferred operator: ")
num2=input("Enter another number: ")

if operator == "+":
    result= int(num1) + int(num2)
elif operator == "-":
    result= int(num1) - int(num2)
elif operator == "*":
    result= int(num1) * int(num2)
elif operator ==  "/":
    result= int(num1) / int(num2)
elif operator == "%":
    result= int(num1) % int(num2)

print(result)
