# Simple Calculator that uses Terminal as a user's screen.
try:
    print("""
        Welcome to simple calculator program by Engr. Ryan!
        This program will guide you through basic arithmetic operations.
        """)

    def MainMenu():
        MainOperation = input("""
            Please select:
            [1] Addition
            [2] Subtraction
            [3] Multiplication
            [4] Division
            Enter your choice: """)
        while True:
            if MainOperation == "1":
                x = int(input("Enter 1st integer: "))
                y = int(input("Enter 2nd integer: "))
                print("Result", Addition(x, y))
                ContinuePrompt()
            elif MainOperation == "2":
                x = int(input("Enter 1st integer: "))
                y = int(input("Enter 2nd integer: "))
                print("Result", Subtraction(x, y))
                ContinuePrompt()
            elif MainOperation == "3":
                x = int(input("Enter 1st integer: "))
                y = int(input("Enter 2nd integer: "))
                print("Result", Multiplication(x, y))
                ContinuePrompt()
            elif MainOperation == "4":
                x = int(input("Enter 1st integer: "))
                y = int(input("Enter 2nd integer: "))
                print("Result", Division(x, y))
                ContinuePrompt()
            else:
                print("Syntax Error")
                MainMenu()

    def ContinuePrompt():
        ContinueOperation = input(
            "Would you like to try another operation [y/n]: ")
        if ContinueOperation == "y":
            MainMenu()
        elif ContinueOperation == "n":
            exit()
        else:
            print("Syntax Error")
            ContinuePrompt()

    def Addition(x, y):
        return x + y

    def Subtraction(x, y):
        return x - y

    def Multiplication(x, y):
        return x * y

    def Division(x, y):
        if y == 0:
            print("Math Error")
        else:
            return x / y

    MainMenu()
except ValueError:
    print("Do not enter a non-integer value!")
    MainMenu()
