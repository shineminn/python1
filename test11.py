while True:
    num1 = int (input ("Enter your first number: "))
    num2 = int (input ("Enter your second number: "))
    choice = input ("Choice these item: +, -, *, /: ")
    if choice == ("+"):
        print (num1 + num2)
    elif choice == ("-"):
        print (num1 - num2)
    elif choice == ("*"):
        print (num1 * num2)
    elif choice == ("/"):
        print (num1 / num2)
    else:
        print ("please enter +, -, *, /")