# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

def perform_operation(num1, num2, operation):
    if operation == "add":
        result = num1 + num2
        return result
    elif operation == "subtract":
        result = num1 - num2
        return result  
    elif operation == "multiply":
        result = num1 * num2
        return result
    elif operation == "divide" and num2 != 0 :
        result = num1 / num2  
        return result
    elif  num2 == 0 and operation == "divide":
         result = "The denominator can not be zero"
         return result
    
# print(perform_operation(num1,num2,operation))