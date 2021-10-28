print("Welcome To The Calculator vr 1.20.3")
while True:
    print("Please Enter The Operation Sign"
          "\n+ For Addition"
          "\n- For Subtraction"
          "\n* For Multiplication"
          "\n/ For Division"
          "\n% For Percentage")
    x = input("What Do You Want To Do: ")
    if x == '+':
        a = float(input("Enter Number 1: "))
        b = float(input("Enter Number 2: "))
        print("Total is: ", a + b)
    if x == '-':
        a = float(input("Enter Number 1: "))
        b = float(input("Enter Number 2: "))
    if x == '*':
        a = float(input("Enter Number 1: "))
        b = float(input("Enter Number 2: "))
        print("Total is: ", a * b)
    if x == '/':
        a = float(input("Enter Number 1: "))
        b = float(input("Enter Number 2: "))
        print("Total is: ", a // b)
    if x == '%':
        a = float(input("Enter Numerator: "))
        b = float(input("Enter Denominator: "))
        z = a / b
        y = z*100
        print("Total is: ", y, "%")
    m = str(input("Enter: "))
    if m != "Exit" or "EXIT" or "exit":
        continue
    else:
        print("Thank You For Using This Calculator")
        break