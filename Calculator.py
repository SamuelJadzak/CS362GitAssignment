def calculator(num1,num2):
    add = num1+num2
    subtract = num1-num2
    multiply = num1*num2
    divide = num1/num2
    print("sum:", add, " difference:", subtract, " product:", multiply, " quotient:", int(divide))
number1 = input("please enter first number")
number2 = input("please enter second number")
calculator(int(number1),int(number2))