import math
Binary = ["+", "-", "/", "%", "*"]
Unary = ["log", "sqrt", "sin", "cos", "tan"]
operator = input("Enter type of operator? (Binary or Unary): ")
if operator == "Binary":
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter a number: "))
    Binaryoperator = input("Choose a opertaor: ")
    if Binaryoperator == "+":
        add = number1 + number2
        print(add)
    elif Binaryoperator == "-":
        sub = number1 - number2
        print(sub)
    elif Binaryoperator == "/":
        div = number1 / number2
        print(div)
    elif Binaryoperator == "*":
        multi = number1 * number2
        print(multi)
    elif Binaryoperator == "%":
        modulus = number1 % number2
        print(modulus)
elif operator == "Unary":  
    Num = int(input("Enter a positive number: "))     
    Unaryoperator = input("Enter a Unary operator: ")
    if Unaryoperator == "sqrt":
        sqroot = math.sqrt(Num)
        print(sqroot)
    elif Unaryoperator == "log" and Num > 1:
        logarithm = math.log(Num)
        print(logarithm)
    elif Unaryoperator == "sin" :
        Num1 = math.radians(Num)
        val1 = math.sin(Num1)
        print(val1)
    elif Unaryoperator == "cos":
        Num2 = math.radians(Num)
        val2 = math.cos(Num2)
        print(val2)
    elif Unaryoperator == "tan":
        Num3 = math.radians(Num)
        val3 = math.tan(Num3)
        print(val3)        
else:
    print("Read properly and enter a correct value.")




              






              


